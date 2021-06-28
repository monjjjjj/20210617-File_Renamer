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
        os.chdir(directory)
        files = os.listdir()
        for filename in files:
            new_name = re.sub(r"{0}".format(pattern), r"{0}".format(replace), filename)
            print(filename, '>>', new_name)
            os.rename(filename, new_name)


# 1F
# os.chdir('7F-1') # John goes to 7F-1 from 1F
# files = os.listdir('7F-1') # John takes a picture of 7F-1 from 1F

# os.chdir('7F-1') # John goes to 7F-1 from 1F
# files = os.listdir() # John takes a picture

#########################################################################

# 7F
# os.chdir('-1') # John goes to room 1
# files = os.listdir('-1') # John takes a picture of room 1 of this room

# os.chdir('-1') # John goes to 7F-1 from 1F
# files = os.listdir() # John takes a picture


