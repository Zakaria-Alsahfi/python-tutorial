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
    # for line in file:
    #     print(line, end='')  # (end='') to delete the space between lines
    # to read line by line
    # all lines
    # file_contents = file.readlines()
    # one line
    #file_contents = file.readline()
    # print(file_contents, end='')

    # if we want to read by the size of the file
    size_to_read = 100
    file_contents = file.read(size_to_read)
    # to find the read postion in the file
    print(file.tell())  # 100
    # to change the read position to any location in the file
    # file.seek(3)
    while len(file_contents) > 0:
        print(file_contents, end='')
        # if we dont add this will get ininfint loop
        file_contents = file.read(size_to_read)
#----------------------------------------------------------------------------

# writing to file
# this way will create a new file and write to it. it will not overwrite an existing file only if we use 'i' insted of 'w'
# with open('test2.txt', 'w') as f:
#     f.write('Hello Python this is just a test.')
#     # to set the postion of the write location f.seek(0)
#     f.write('I am really glad to know you.')

# to copy from a file and write to another
# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# to copy picture file
# with open('abody.jpg', 'rb') as rf:
#     with open('abody_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# to cope a large picture file
with open('abody.jpg', 'rb') as rf:
    with open('abody_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
