# Cool Commits

## What?
Let's find the coolest commits hashes in the world!

Every commits has a short hash format that looks like: `fc5202c`.
Sometimes it looks **cool**: `6661666` / `2121212` / `aaa6aaa`.

I made this small project because I'm obsessed with finding cool commits, every commit I do,
I'm wishing I'll have something cool, most of the time my heart breaks :(

## Requirements
- Python3.5 or higher
- A absolute path of a directory with git repo in it

## Installation
`pip install cool-commits`

## Executing
If you want the **TL;DR** version, with only the hash as a list, run:

`python -m cool_commits find /path/to/directory/with/git`

This will print something like:

`6661666 aaa6aaa`

Each commit represent the coolest commit from each `parser`(algorithm/pattern)

If you want more info about the commit and the `parser`, run:

`python -m cool_commits info /path/to/directory/with/git`

This will print:
```
============================================================

Commit hash: 6661666
Commit parser: < MostCommon >

Trying to find a commit with highest most common repeated char.
For example:
1231114 - has rank of 4, because `1` is the most common char.

commit 6661666fe6aa59cb901027d14013d46b28f2de76
Author: Author Name <myname@gmail.com>
Date:   Thu Mar 9 16:00:45 2017 -0800

    Added command line interfaces for future refactoring

============================================================

Commit hash: aaa6aaa
Commit parser: < Consecutive >

Trying to find a commit with highest consecutive chars.
For example:
1231114 - has rank of 3, because `1` is consecutive 3 the most.

commit aaa6aaabfc870671fcc4075845d002438462c34e
Author: Author Name <myname@gmail.com>
Date:   Mon Nov 10 00:45:13 2014 -0800

    Raising an error when the user has an invalid input

============================================================
```
## Using `cool_commit` module form code
if you want to integrate the cool_coomit output into your code, you can import the same function as in the command line tool like this:
```
from cool_commits import find, info

# Returning a commit hash for each parser's commit
print(*find('/path/to/directory/with/git'))

# Returning a text info for each parser's commit
print(*info('/path/to/directory/with/git'))
```

## Writing your own parser
*Author note: If you think your parser is cool, submit it as a PR, or by email to: orduani@gmail.com*

If you want to add your own parser, all you need to do is write custom class, that inherit from `BaseParser`  and implement the `parse` method:
```
from cool_commits.parsers import BaseParser

class TestParser(BaseParser):
    description = "Optional description that describe how your parser works"
    
    def parse(self, commits):
        # Write here you logic. `commits` is a list of str commits
        # For this example, my parser will return the first commit,
        # in reality, you want to iterate over the commits and return
        # the coolest one.
        return commits[0]
        
# To use it, call the find/info functions
print(find('/path/to/directory/with/git'))
```
