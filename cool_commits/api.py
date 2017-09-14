from cool_commits.parsers import all_parsers
from cool_commits.utils import git_all_commits


def find(path):
    commits_list = git_all_commits(path)

    for parser in all_parsers:
        yield str(parser(commits_list, path))


def info(path):
    commits_list = git_all_commits(path)

    for parser in all_parsers:
        yield parser(commits_list, path).info()
