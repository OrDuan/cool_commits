from cool_commits.parsers import BaseParser
from cool_commits.utils import git_all_commits


def find(path):
    commits_list = git_all_commits(path)

    for parser in BaseParser.children:
        yield str(parser(commits_list, path))


def info(path):
    commits_list = git_all_commits(path)

    for parser in BaseParser.children:
        yield parser(commits_list, path).info()
