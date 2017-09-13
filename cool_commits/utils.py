import subprocess


def git_all_commits(path):
    try:
        p = subprocess.run('git log --pretty=format:"%h"', shell=True, stdout=subprocess.PIPE, cwd=path)
    except FileNotFoundError:
        raise FileNotFoundError(f'No such directory: "{path}"') from None
    return p.stdout.splitlines()


def git_commit_info(commit_hash, path):
    try:
        p = subprocess.run(f'git show {commit_hash} --no-patch', shell=True, stdout=subprocess.PIPE, cwd=path)
    except FileNotFoundError:
        raise FileNotFoundError(f'No such directory: "{path}"') from None
    return p.stdout.decode()


