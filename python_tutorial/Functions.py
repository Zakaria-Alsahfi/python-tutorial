#-------------------------------------------------------
def hello_func():
  #print('Hello Function!')
  return 'Hello Function!'


print(hello_func().upper())         # HELLO FUNCTION!
print(hello_func().lower())         # hello function!
#-------------------------------------------------------
# pass argumnet to a function


def hello_func(greeting):
  return '{} Function.'.format(greeting)


print(hello_func('Hello New'))       # Hello New Function.
#-------------------------------------------------------
# pass arguments with defualt value


def hello_func(greeting, name='Python'):
  return '{}, {}'.format(greeting, name)


print(hello_func('Hello'))           # Hello, Python
print(hello_func('Hello', name='Python 3'))  # Hello, Python 3
#-------------------------------------------------------
# function to allow us to accept an arbitray number of positional or keyword arguments


def student_info(*args, **kwargs):
  print(args)
  print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info('Math', 'Art', name='John', age=22)
student_info(*courses, **info)
#-------------------------------------------------------
