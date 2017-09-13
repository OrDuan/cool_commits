import sys

from cool_commits import info, find

if __name__ == '__main__':
    command = sys.argv[1]
    if command == 'find':
        print(*find(sys.argv[2]))
    elif command == 'info':
        for info_text in info(sys.argv[2]):
            print('='*60)
            print(info_text)
        print('='*60)
    else:
        raise IOError('Invalid command, supporting only `find` and `info`.')

