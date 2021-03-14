student = {'name' : 'luiz', 'age': 23,'courses': ['Math', 'CompSci']}
print(student['name'])
print(student.get('name'))
student['phone'] = '555'
student['name'] = 'jane'
print(student)
student.update ({'name': 'Jane', 'age':26, 'phone': '555-5555'})
print(student)
del student['age']
print(student)

age = student.pop('phone')
print(student)
print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)