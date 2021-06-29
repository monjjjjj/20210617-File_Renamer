import argparse
import re
import os.path
import sys


def get_parser():
    parser = argparse.ArgumentParser(description='Just a test!')
    parser.add_argument("directory", help="Directory of files.")
    parser.add_argument("pattern",
                        help="Please input the regular expression of the files. "
                             "Please refer to the following website."
                             "https://docs.python.org/3/library/re.html")
    parser.add_argument("replacement", help="Please input the group of replacement.")
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    direct = args.directory
    patt = args.pattern
    replace = args.replacement

    print(direct)

    if not os.path.isdir(direct):
        print("The path does not exist!")
    else:
        os.chdir(direct)
        files = os.listdir(".")    # dot = current directory
        for filename in files:
            new_name = re.sub(r"{0}".format(patt), r"{0}".format(replace), filename)
            print(filename, '>>', new_name)
            os.rename(filename, new_name)
