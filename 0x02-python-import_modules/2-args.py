#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = ' '.join(sys.argv[1:])

    args_list = argv.split()

    argc = len(args_list)

    if argc == 0:
        print('0 arguments.')
    else:
        print('{} argument{}:'.format(argc, 's' if argc > 1 else ''))
        for i, argv in enumerate(args_list, 1):
            print('{}: {}'.format(i, argv))
