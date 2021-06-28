import re
import os.path
import sys

if __name__ == "__main__":

    directory = sys.argv[1]
    pattern = sys.argv[2]
    replace = sys.argv[3]

    if not os.path.isdir(directory):
        print("The path does not exist!")
    else:
        os.chdir(r"%s" % directory)
        files = os.listdir(directory)
        for filename in files:
            new_name = re.sub(r"{0}".format(pattern), r"{0}".format(replace), filename)
            print(filename, '>>', new_name)
            os.rename(filename, new_name)
