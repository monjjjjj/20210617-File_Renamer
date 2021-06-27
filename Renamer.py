import re
import glob
import os.path
import sys

if __name__ == "__main__":

    direct = sys.argv[1]

    if os.path.isdir(direct):
        print("The path exists!")
    else:
        print("The path does not exist!")

    file = glob.glob(r"%s/*" % direct)

    for filename in file:
        new_name = re.sub(r"({0}/){1}".format(direct, sys.argv[2]), r"{0}".format(sys.argv[3]), filename)
        os.rename(filename, new_name)
print("Rename done!")
