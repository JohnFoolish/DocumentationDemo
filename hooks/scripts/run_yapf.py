import re
import sys
import subprocess
from pathlib import Path
"""
Git hook script to format Python files using YAPF
"""

# REGEX for matching branch names
BRANCH_REGEX = re.compile(".*")
# BRANCH_REGEX = re.compile("master")

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

    try:
        import yapf
    except ModuleNotFoundError:
        print("yapf not found; can not format. Please install yapf:")
        print("    pip install yapf")
        sys.exit(1)

    # Check for unstaged changes to files in the index.
    out = subprocess.run(["git", "diff", "--name-only", "--"] +
                         [str(f) for f in python_files],
                         stdout=subprocess.PIPE)
    changed = [
        str(Path(f))
        for f in out.stdout.decode(sys.stdout.encoding).splitlines()
    ]
    if len(changed) > 0:
        print(
            "You have unstaged changes to some files in your commit; skipping "
        )
        print(
            "auto-format. Please stage, stash, or revert these changes. You may "
        )
        print("find `git stash -k` helpful here.")
        print(f"Files with unstaged changes: {' '.join(changed)}")
        sys.exit(1)

    # Format all staged files, then exit with an error code if any have uncommitted changes.
    print("Formatting staged Python files . . .")

    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         stdout=subprocess.PIPE)
    repo_root = Path(out.stdout.decode(sys.stdout.encoding).splitlines()[0])
    python_files = [str(repo_root / f) for f in python_files]
    out = yapf.main(["yapf", "-i", "-r"] + python_files)
    if out != 0:
        sys.exit(out)

    out = subprocess.run(["git", "diff", "--name-only", "--"] +
                         [str(f) for f in python_files],
                         stdout=subprocess.PIPE)
    changed = [
        str(Path(f))
        for f in out.stdout.decode(sys.stdout.encoding).splitlines()
    ]
    if len(changed) > 0:
        print("Reformatted staged files. Please review and stage the changes.")
        print(f"Files updated: {' '.join(changed)}")
        sys.exit(1)
