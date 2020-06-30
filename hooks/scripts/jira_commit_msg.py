import re
import sys
import subprocess
from pathlib import Path
"""
Git hook script to check the branch name for a Jira id and add it to the commit message
"""

# REGEX for matching Jira ids in branch name prefix
JIRA_ID_REGEX = re.compile("([^/]+/)*[A-Z0-9]{1,10}-?[A-Z0-9]+")

if __name__ == "__main__":
    commit_file = Path(sys.argv[1])
    commit_msg = commit_file.read_text()

    out = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                         stdout=subprocess.PIPE)
    current_branch = out.stdout.decode(sys.stdout.encoding).splitlines()[0]

    cur_branch_name = JIRA_ID_REGEX.match(current_branch)
    commit_msg = JIRA_ID_REGEX.match(commit_msg)

    if commit_msg is not None:
        if cur_branch_name is not None:
            jira_id_msg = commit_msg.group()
            jira_id_name = cur_branch_name.group()
            if jira_id_msg != jira_id_name:
                print(
                    f"Error, your commit message JIRA_TASK_ID='{jira_id_msg}' is not equal to current branch JIRA_TASK_ID='{jira_id_name}'"
                )
                sys.exit(1)
    elif cur_branch_name is not None:
        jira_id = cur_branch_name.group()
        commit_file.write_text(f"{jira_id} {commit_msg}")
        print(
            f"JIRA ID '{jira_id}', matched in current branch name, prepended to commit message. (Use --no-verify to skip)"
        )
