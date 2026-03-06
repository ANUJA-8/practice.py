# import os
# print(os.getcwd())

f=open('file.txt')
# to read the data upto given index
# print(f.read(4))
line=f.readline()

# to read the lines with space
# while line!="":
#     print(line)
#     line= f.readline()

#to print the lines in list form
for line in f.readlines():
    print(line)
f.close()