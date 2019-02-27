# Sets are value that unordered and also have no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(art_courses.difference(cs_courses))
print(cs_courses.union(art_courses))

# Create an empty Sets
empty_set = {}  # This isn't right it's  to create an empty Dictionary
empty_set = set()
