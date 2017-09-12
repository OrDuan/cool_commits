import subprocess
from collections import Counter


def main(path):
    try:
        p = subprocess.run('git log --pretty=format:"%h"', shell=True, stdout=subprocess.PIPE, cwd=path)
    except FileNotFoundError:
        raise FileNotFoundError(f'No such directory: "{path}"') from None

    commits_list = p.stdout.splitlines()

    for version in (version1, version2, version3):
        most_common = version(commits_list)
        print(most_common[0])


def version3(commits):
    most_common = ('', 10)
    for commit in commits:
        current_most = set(commit)
        if len(current_most) < most_common[1]:
            most_common = (commit, len(current_most))

    return most_common


def version2(commits):
    most_common = ('', 0)
    for commit in commits:
        current_most = 0
        for i, ch in enumerate(commit[:-1]):
            if ch == commit[i + 1]:
                current_most += 1
        if current_most > most_common[1]:
            most_common = (commit, current_most)

    return most_common


def version1(commits):
    most_common = ('', 0)
    for commit in commits:
        current_most = Counter(commit).most_common()[1][1]
        if current_most > most_common[1]:
            most_common = (commit, current_most)
    return most_common


if __name__ == "__main__":
    main('/')
