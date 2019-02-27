# Lists
courses = ['History','Math','Physics','CompSci']
courses_2 = ['Education','Religion']
print(courses)
print(len(courses))
print(courses[:4])
print(courses[-1])

#List Methoud
courses.append('Art')
courses.insert(0, 'Computer')
courses.extend(courses_2)
print(courses)

# remove From List
courses.remove('Math')
popped = courses.pop()
print(popped)
print(courses)

# sort a List
courses.reverse()
print(courses)
nums = [1,5,2,4,3]
nums.sort()
nums.sort(reverse = True)
sorted_coueses = sorted(courses)
print(nums)
print(sorted_coueses)


# Min Max and sum
print(min(nums))
print(max(nums))
print(sum(nums))

#search in List
print(courses.index('Art'))
print('Art' in courses)


# for loop
for course in courses:
	print(course)

#print value with index number
for index, course in enumerate(courses,  start = 1):
	print(index, course)

#turn List into String
courses_str = ' - '.join(courses)
new_list = courses_str.split(' - ')
print(courses_str)
print(new_list)




