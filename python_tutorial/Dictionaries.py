student = {'name': 'Jone', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name'])
# if the key doesn't exists
print(student.get('phone', 'Not Found'))

# to Add new entry to Dictionary
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))

# to update a value in the Dictionary
student['name'] = 'Ahmad'
print(student['name'])

# to update multiple values
student.update({'name': 'Zakaria', 'age': 32, 'phone': '3144150113'})
print(student)

# to delete a specific key and its value
del student['phone']
print(student)

# delete using pop methoud
age = student.pop('age')
print(student)
print(age)

# to loop theough all the keys and values in the Dictionary we have two way

# 1- Methoud
# find how many keys
print(len(student))
# to see all keys or values
print(student.keys())
print(student.values())
# to see both keys and values
print(student.items())

# 2- For-Loop
# to print keys
for key in student:
  print('keys:' + key)

# to print values
  for value in student:
    print('value:' + value)

# to print both keys and values
for key, value in student.items():
  print(key, value)
