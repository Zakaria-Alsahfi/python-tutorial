# OS Module allows us to interact with the underlying operating system in several different ways for example we can navigate the file system get file information look up and change the environment variables we can move files around.

import os
from datetime import datetime
# to see all the attributes and methods within module
print(dir(os))

# to get current working directory
print(os.getcwd())

# to navigate to a new location on the file system
os.chdir('/Users/zakariaalsahfi/Documents/')
print(os.getcwd())

# to see file and folders in a directory
print(os.listdir())

# to create a new folder in a directory there are two ways
# both are similar but makedirs() if we want to create that a few levels deep (folder inside a folder) and mkdir() will create all of the intermediate level directories (folder)
# 1
os.mkdir('python-tutorial-1')
# 2
os.makedirs('python-tutorial-2/new-1')
print(os.listdir())

# to delete a file or folder in a directory there are two ways
# both are similar but removedirs() if we want to create that a few levels deep (folder inside a folder) and rmdir() will create all of the intermediate level directories (folder)
# 1
os.rmdir('python-tutorial-1')
# 2
os.removedirs('python-tutorial-2/new-1')
print(os.listdir())

# to rename a file or folder
os.rename('python-tutorial-1', 'python-tutorial-3')
print(os.listdir())

# to see infromation about a file or folder
print(os.stat('python-tutorial-3'))

# attributes:
# ast_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime
# for example if we want modifide time
mod_time = os.stat('python-tutorial-3').st_mtime
print(datetime.fromtimestamp(mod_time))

# to see the entire directory tree and files within a directory
# if we want to traverse the diractory tree and print all of the directories and the files.
for dirpath, dirnames, filenames in os.walk('/Users/zakariaalsahfi/Documents/'):
    print('Current Path:', dirpath)
    print('Direvtories:', dirnames)
    print('Files:', filenames)
    print()
# get environment variable let's say we want to access home diractory location by grabbing the home environment variable
print(os.environ.get('HOME'))

# to combine a directory with a filename
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# to grab the file name or diractory anme of any path or both
os.path.basename('/temp/test.txt')  # test.txt
os.path.dirname('/temp/test.txt')  # /temp
os.path.split('/temp/test.txt')  # ('/temp', 'test.txt')

# to check if a path exists or not
os.path.exists('/temp/test.txt')  # return True or False

# to check if somthing is a directory or file
os.path.isdir('/temp/test.txt')  # return True or False
os.path.isfile('/temp/test.txt')  # return True or False

# to split the root of the path and extension
os.path.splitext('/temp/test.txt') # ('/temp/tes', 't.txt')
