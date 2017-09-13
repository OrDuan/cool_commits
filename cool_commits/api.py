from cool_commits.parsers import BaseParser
from cool_commits.utils import git_all_commits


def find(path):
    commits_list = git_all_commits(path)
    yield from get_most_common(commits_list, path)


def info(path):
    for parser in find(path):
        print('=' * 60)
        print(parser.info())
    print('=' * 60)


def get_most_common(commits_list, path):
    for parser in BaseParser.children:
        yield parser(commits_list, path)
