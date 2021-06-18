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
###################################################################
string = "Chloe_File_1"
regex = re.compile(r"([A-Z]).*_([A-Z]).*_(\d)")
match = regex.search(string)
match2 = regex.findall(string)
# match = re.compile(r"段(\d+-*\d*)").search(string)
print(match.group(1, 2, 3))
print(match2)
###################################################################
string2 = "今天的日期是：2020-07-01 14:02:48"

time = re.search(r'\d+-\d+-\d+ \d+:\d+:\d+', string2).group()
print(time)
###################################################################
regex1 = re.compile(r"(\w)(\W)")
find = regex1.findall("A/1$5&6")
print(find)

for match in regex1.finditer("A/1$5&"):
    print(match.group(1), match.group(2))