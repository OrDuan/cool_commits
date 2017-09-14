import subprocess


def git_all_commits(path):
    try:
        p = subprocess.run('git log --pretty=format:"%h"', shell=True, stdout=subprocess.PIPE, cwd=path)
    except FileNotFoundError:
        raise FileNotFoundError('No such directory: "{}"'.format(path)) from None
    return p.stdout.decode().splitlines()


def git_commit_info(commit_hash, path):
    try:
        command = 'git show {} --no-patch'.format(commit_hash)
        p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, cwd=path)
    except FileNotFoundError:
        raise FileNotFoundError('No such directory: "{}"'.format(path)) from None
    return p.stdout.decode()


