
nums = [1, 2, 3, 4, 5]

# For-Loop
for num in nums:
  print(num)

# Keywords in For_loop
# 1- brake
for num in nums:
  if num == 3:
    print('Found it')
    break
  print(num)

# 2- continue
for num in nums:
  if num == 5:
    print('Found it')
    continue
  print(num)

  # loop within a loop
  for num in nums:
    for letter in 'ab':
      print(num, letter)

  # loop with certain number of times
  for x in range(1, num):
    print(x)


# While loop
x = 1
while x <= 5:
  print(x)
  x += 1

# infinite loop
y = 0
while True:
  if y == 5:
    break
  print(y)
  x += 1
