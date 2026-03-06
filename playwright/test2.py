#read the file store all lines in list 
#reverse the list
#add the reversed lis in file

with open('file.txt','r') as reader:
    content= reader.readlines()
    reversed(content)
    with open('file.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)