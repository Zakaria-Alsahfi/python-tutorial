# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is  (Check if two objects have the same Id which means if they are the same object in memory)

language = 'Python'
# Case Sensitive
# if Statement
if language == 'Python':
  print('Conditional was True')

# if else Statement
if language == 'Python':
  print('Language is ' + language)
else:
  print('Language is Not match')

# to check multiple conditions using l-lif
if language == 'Python':
  print('Language is ' + language)
elif language == 'Java':
  print('Language is ' + language)
else:
  print('Language is Not match')

# Boolean Operations (and , or ,not)
user = 'Admin'
logged_in = False

# and
if user == 'Admin' and logged_in:
  print('Admin Page')
else:
  print('bad Creds')
# or
if user == 'Admin' or logged_in:
  print('Admin Page')
else:
  print('bad Creds')

# not
if not logged_in:
  print('Please Log In')
else:
  print('Welcome')


# the diffrent between '==' and 'is'
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False
# get location in memory
print(id(a))
print(id(b))


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = False

if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')
