from collections import Counter
from textwrap import dedent
from typing import List

from cool_commits.utils import git_commit_info

# A list of instances of BaseParser, this way
# we can auto discover al inherited parsers
all_parsers = []


class BasePaerserMeta(type):
    def __init__(cls, name, bases=None, object=None):
        if name != 'BaseParser':
            all_parsers.append(cls)
        super().__init__(object)


class BaseParser(metaclass=BasePaerserMeta):
    description = None

    def __init__(self, commits, path):
        self.path = path
        self.commit = self.parse(commits)

    def parse(self, commits: List[str]) -> str:
        raise NotImplementedError

    def __str__(self):
        return self.commit

    def __repr__(self):
        return '< {} >'.format(self.__class__.__name__)

    def info(self) -> str:
        data = dict(
            hash=self.__str__(),
            parser=self.__repr__(),
            description=dedent(self.description if self.description else ''),
            commit_info=git_commit_info(self.commit, self.path),
        )
        text = """
Commit hash: {hash}
Commit parser: {parser}
{description}
{commit_info}
""".format(**data)
        return text.strip()


class MostCommonParser(BaseParser):
    description = """
        Trying to find a commit with highest most common repeated char.
        For example:
        1231114 - has rank of 4, because `1` is the most common char.  
    """

    def parse(self, commits):
        most_common = ('', 0)

        for commit in commits:
            current_most = Counter(commit).most_common()[0][1]
            if current_most > most_common[1]:
                most_common = (commit, current_most)
        return most_common[0]


class ConsecutiveParser(BaseParser):
    description = """
        Trying to find a commit with highest consecutive chars.
        For example:
        1231114 - has rank of 3, because `1` is consecutive 3 the most.  
    """

    def parse(self, commits):
        most_common = ('', 0)
        for commit in commits:
            current_most = 0
            for i, ch in enumerate(commit[:-1]):
                if ch == commit[i + 1]:
                    current_most += 1
            if current_most > most_common[1]:
                most_common = (commit, current_most)

        return most_common[0]
