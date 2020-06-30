#!/usr/bin/env python

import os
import sys
import stat
import subprocess
from pathlib import Path
from shutil import copyfile

HOOK_TYPES = [
    "applypatch-msg", "commit-msg", "post-applypatch", "post-checkout",
    "post-commit", "post-merge", "post-receive", "post-rewrite", "post-update",
    "pre-applypatch", "pre-auto-gc", "pre-commit", "pre-push", "pre-rebase",
    "pre-receive", "prepare-commit-msg", "update"
]


def my_print(msg):
    print(f"[Py-Autohook] {msg}")


def install():
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         stdout=subprocess.PIPE)
    repo_root = Path(out.stdout.decode(sys.stdout.encoding).splitlines()[0])
    hooks_dir = repo_root / ".git" / "hooks"
    autohook_linktarget = repo_root / "hooks" / "autohook.py"

    for hook_type in HOOK_TYPES:
        hook_symlink = hooks_dir / hook_type
        # Symlinks are difficult to reliably create on Windows
        # For now just copy the file
        copyfile(autohook_linktarget, hook_symlink)
        st = os.stat(hook_symlink)
        os.chmod(hook_symlink, st.st_mode | stat.S_IEXEC)


def run_hooks(hook_type, args):
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         stdout=subprocess.PIPE)
    repo_root = Path(out.stdout.decode(sys.stdout.encoding).splitlines()[0])
    script_dir = repo_root / "hooks" / "scripts"
    hooks_file = repo_root / "hooks" / (hook_type + ".txt")

    if hooks_file.exists():
        hooks = hooks_file.read_text().splitlines()
    else:
        hooks = []

    my_print(f"Looking for {hook_type} scripts to run...found {len(hooks)}!")

    for hook_text in hooks:
        hook_text = hook_text.split()
        if len(hook_text) != 2:
            my_print(
                f"Hook command '{hook_text}' must contain a command and file")
            sys.exit(1)
        hook_cmd = hook_text[0]
        hook_name = hook_text[1]
        hook = script_dir / hook_name
        my_print(f"BEGIN {hook.name}")
        out = subprocess.run([hook_cmd, str(hook)] + args)
        hook_exit_code = out.returncode
        if hook_exit_code != 0:
            my_print(
                f"A {hook_type} script yielded negative exit code {hook_exit_code}"
            )
            sys.exit(hook_exit_code)
        my_print(f"FINISH {hook.name}")


if __name__ == "__main__":
    calling_file = Path(sys.argv[0]).name
    if calling_file in HOOK_TYPES:
        run_hooks(calling_file, sys.argv[1:])
    else:
        install()
