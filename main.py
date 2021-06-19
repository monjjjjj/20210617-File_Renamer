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
pattern = re.compile(r"hell")
a = re.match(pattern, "hello world")
b = re.search(pattern, "world hello")
c = re.search(pattern, "hell")
d = re.match(pattern, "hello")
print(a.group())
print(b.group())
print(c.group())
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

time = re.search(r'\d+-\d+-\d+ \d+:\d+:\d+', string2).group(0)
print(time)
###################################################################
# findall vs group
regex1 = re.compile(r"(\w)(\W)")
find = regex1.findall("A/1$5&6")
print(find)

for match in regex1.finditer("A/1$5&"):
    print(match.group(1), match.group(2))
###################################################################
text2 = '編輯 - 衛斯理ggggg 小編'

author = re.search('- (.*?) ', text2).group(1)  # 為啥要有問號？如果單純是.*不行嗎？
print(author)

author = re.search('- (\w+)', text2).group(1)
print(author)

###################################################################
# re.match跟re.search差在，re.match是檢測文字是否在開頭位置
text1 = '賴清德選上副總統！'

name = re.match(r'賴清德', text1).group(0)
print(name)