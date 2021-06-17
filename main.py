# ShellExecutePython
# import os
import re

# RenameFile
# old_file_name = "/Users/chloe/Desktop/20210617 File_Renamer/Chloe_File_1.xlsx"
# new_file_name = "/Users/chloe/Desktop/20210617 File_Renamer/C_File_1.xlsx"

# os.rename(old_file_name, new_file_name)

# print("File renamed!")

# RegularExpression
# a = re.match("abcd", "abcdefghijk").group()
# print(a)
pattern = re.compile(r"hello")
a = re.match(pattern, "hello world")
b = re.match(pattern, "world hello")
c = re.match(pattern, "hell")
d = re.match(pattern, "hello")
print(a.group())
# print(b.group())
# print(c.group())
print(d.group())

string = "臺中市南屯區埔興段35-12地號"
regex = re.compile(r"段(\d+-*\d*)")
match = regex.search(string)
print(match.group(1))
