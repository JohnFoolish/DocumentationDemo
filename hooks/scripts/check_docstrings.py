import re
import sys
import types
import subprocess
from pathlib import Path
from runpy import run_path
"""
Git hook script to check Python files for missing docstrings
"""

# Will reject commit if STRICT = True and docstring is missing
# If STRICt = False will just print a message
STRICT = False

# REGEX for matching branch names
BRANCH_REGEX = re.compile(".*")
# BRANCH_REGEX = re.compile("master")


def check_docstrings(file):
    try:
        attrs = run_path(str(file))
    except Exception as e:
        print(f"File {str(file)} failed to load with exception:")
        print(e)
        if STRICT:
            sys.exit(1)
        return

    for key in attrs.keys():
        if key[0] == "_":
            # Do not check for docstrings on private attributes
            continue
        obj_name = f"{file.stem}.{key}"
        val = attrs[key]
        if isinstance(val, type):
            doc = val.__doc__
            if doc is None:
                print(f"Public class {obj_name} has no docstring")
                if STRICT:
                    sys.exit(1)
            cls_attrs = val.__dict__
            for cls_key in cls_attrs.keys():
                if cls_key[0] == "_":
                    continue
                cls_obj_name = f"{file.stem}.{key}.{cls_key}"
                cls_val = cls_attrs[cls_key]
                if isinstance(cls_val, types.FunctionType):
                    doc = cls_val.__doc__
                    if doc is None:
                        print(
                            f"Public class method {cls_obj_name} has no docstring"
                        )
                        if STRICT:
                            sys.exit(1)
        elif isinstance(val, types.FunctionType):
            doc = val.__doc__
            if doc is None:
                print(f"Public function {obj_name} has no docstring")
                if STRICT:
                    sys.exit(1)


if __name__ == "__main__":
    # Check branch name
    out = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                         stdout=subprocess.PIPE)
    branch_name = out.stdout.decode(sys.stdout.encoding).splitlines()[0]

    if BRANCH_REGEX.fullmatch(branch_name) is None:
        sys.exit(0)

    # Find all staged Python files, and exit early if there aren't any.
    out = subprocess.run(
        ["git", "diff", "--name-only", "--cached", "--diff-filter=AM"],
        stdout=subprocess.PIPE)
    staged = [
        Path(f) for f in out.stdout.decode(sys.stdout.encoding).splitlines()
    ]
    python_files = [f for f in staged if f.suffix == ".py"]
    if len(python_files) == 0:
        sys.exit(0)

    # Check for unstaged changes to files in the index.
    out = subprocess.run(["git", "diff", "--name-only", "--"] +
                         [str(f) for f in python_files],
                         stdout=subprocess.PIPE)
    changed = [
        Path(f) for f in out.stdout.decode(sys.stdout.encoding).splitlines()
    ]

    if len(changed) > 0:
        print(
            "You have unstaged changes to some files in your commit; skipping "
        )
        print(
            "dosctring check. Please stage, stash, or revert these changes. You may "
        )
        print("find `git stash -k` helpful here.")
        print(
            f"Files with unstaged changes: {' '.join([str(f) for f in changed])}"
        )
        sys.exit(1)

    # Check docstrings in all staged files
    # Exit with an error code if STRICT == True and any documentation is missing
    # Otherwise print a warning message
    print("Checking documentation in staged Python files . . .")

    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         stdout=subprocess.PIPE)
    repo_root = Path(out.stdout.decode(sys.stdout.encoding).splitlines()[0])
    python_files = [repo_root / f for f in python_files]

    for file in python_files:
        check_docstrings(file)
