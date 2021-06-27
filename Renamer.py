import re
import glob
import os
import os.path
import sys


# file = glob.glob(r"/Users/chloe/Desktop/20210617 File_Renamer/*.xlsx")
# for filename in file: new_name = re.sub(r"(/Users/chloe/Desktop/20210617 File_Renamer/)([A-Z]).*_([A-Z]).*_(\d)",
# r"\g<1>\g<2>_\g<3>_\g<4>", filename) print(filename, new_name) os.rename(filename, new_name)

if __name__ == "__main__":

    def folder_path():
        while True:
            path = input("The path of files: ")
            if os.path.isdir(path):
                return str(path)
            else:
                print("The path does not exist!")


    direct = sys.argv[1]
    # directory = folder_path(direct)
    file = glob.glob(r"%s/*" % direct)

    for filename in file:
        new_name = re.sub(r"({0}/){1}".format(direct, sys.argv[2]), r"{0}".format(sys.argv[3]), filename)
        print(r"({0}){1}".format(direct, sys.argv[2]), r"{0}".format(sys.argv[3]), filename)
        print(new_name)
        os.rename(filename, new_name)
