courses = ['History', 'Math', 'Physics','CompSci']
print (courses)
print (len(courses))
print (courses[0])
print (courses[-1])
print (courses[0:2])
print (courses[2:])

courses.append('Art')
print ('add no final: ', courses)

courses.insert(0, 'Art')
print('add na possição 0: ', courses)

courses_2 = ['Education']
courses_2.insert(0, courses)
print(courses_2)

courses.remove('Math')
print('remove especifico: ', courses)

popped=courses.pop()
print('item deletado: ', popped)
print(courses)

courses.reverse()
print('invertida: ',courses)

sorted_courses = sorted(courses)
print('embaralhado: ',sorted_courses)
nums = [1,5,2,4,3]
print(f'max: {max(nums)} min: {min(nums)} soma: {sum(nums)} ')

print(courses.index('Art'))
print('Art' in courses)

for corse in  courses:
    print(corse)

for index, course in enumerate (courses, start=1):
    print(index,course)

course_str = ','.join(courses)
new_list = course_str.split(',')
print('vetor p/ string: ',course_str)
print('string p/ vetor: ',new_list)

list_1 = ['History', 'Math', 'Physics','CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

cs_courses = {'History', 'Math', 'Physics','CompSci'}
art_courses = {'History', 'Math', 'Art','Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))