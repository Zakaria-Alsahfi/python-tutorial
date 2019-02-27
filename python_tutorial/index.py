# ways to import module
import my_module
import my_module as mm

from my_module import find_index
from my_module import find_index
from my_module import find_index as fi
from my_module import test
from my_module import test
# to import evrything the module we use (import my_module *)
# to find where Python looks for modules
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Physics')  # import my_module
index1 = mm.find_index(courses, 'Math')  # import my_module as mm
index2 = find_index(courses, 'History')  # from my_module import find_index
index3 = fi(courses, 'Math')  # from my_module import find_index as fi, test

print(index)
print(index1)
print(index2)
print(test)  # from my_module import find_index, test
print(index3)
print('Modules Path:\n', sys.path)
