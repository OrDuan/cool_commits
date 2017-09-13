import sys

from cool_commits import info, find

if __name__ == '__main__':
    command = sys.argv[1]
    if command == 'find':
        print(*find(sys.argv[2]))
    elif command == 'info':
        info(sys.argv[2])
    else:
        raise IOError('Invalid command, supporting only `find` and `info`.')

