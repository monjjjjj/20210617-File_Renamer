import re
import glob
import os
file = glob.glob(r"/Users/chloe/Desktop/20210617 File_Renamer/*.xlsx")

for filename in file:
    new_name = re.sub(r"(/Users/chloe/Desktop/20210617 File_Renamer/)([A-Z]).*_([A-Z]).*_(\d)", r"\1\2_\3_\4", filename)
    print(filename, new_name)
    os.rename(filename, new_name);