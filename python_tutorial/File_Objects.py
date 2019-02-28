'''Reading and Writing to Files'''

# to open a file
# this open command allows us to specify whether we want to open this file for reading, writing, appending or reading and writing.
# if we dont specify anything then by defualts to open the file for reading

# ways to open a file
# 1- in this way we must close the file
# f = open('test.txt')
# print(f.name)  # test.txt
# print(f.mode)  # r stand for reading
# f.close()

# 2- context mangagers we don't have to use close
with open('test.txt') as file:
    print(file.name)  # test.txt
    print(file.mode)  # r stand for reading
    # to read the entire file if the file is small
    #file_contents = file.read()
    # if we have a big file we should use for-loop
    for line in file:
        print(line, end='') # (end='') to delete the space between lines
    # to read line by line
    # all lines
    # file_contents = file.readlines()
    # one line
    #file_contents = file.readline()
    # print(file_contents, end='')
