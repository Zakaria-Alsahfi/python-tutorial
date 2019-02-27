# tuples are similar to list but we can not modified it

#Mutable
list_1 = ['History','Math','Physics','CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

#Immutable: it can't be change
tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

