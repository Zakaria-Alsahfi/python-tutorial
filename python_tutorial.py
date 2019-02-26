
# to print a simple text
message = 'Hello bobby\'s World'
print(message)
x = 2
y = 2
l = x + y
# to print string with varibles
print('total of: ', x, '+', y, '=', l)

# to print multiple sring lines
message1 = """my world was a good
cartoon in the 1990s """
print(message1)

# find how many carecter in the string
print(len(message1))
# find charecter by index
print(message[0])
print(message[:11])
print(message[13:])

# print lower case
print(message.lower())
print(message.upper())
# find how many times leters or words in a string
print(message.count('b'))
# to replace times leters or words in a string
message = message.replace('World', 'Universe')
print(message)

# combine string
greeting = 'Hello'
name = 'Python'
# wither by +
#message2 = greeting + ' ' + name
# or tplace holder
#message2 = '{},{}. Welcome!'.format(greeting, name)
# or if string
message2 = f'{greeting},{name}. Welcome!'
print(message2)
# to find more method for string
print(help(str))
