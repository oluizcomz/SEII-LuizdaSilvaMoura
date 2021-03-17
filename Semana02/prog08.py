#work with function
def hello_func():
    print('Hello_Function!')

hello_func()

def hello_rfunc():
    return 'Hello_Function!'

print(hello_rfunc())
print(hello_rfunc().upper())

def hello_func(greeting, name ='You'):
    return '{}, {}'.format(greeting,name)

print(hello_func('Hi'))
print(hello_func('Hi', name = 'Corey'))

def student_info(*args,**kwarges):
    print(args)
    print(kwarges)

student_info('Maths','Art',names = 'jhon',age = 22)
couses = ['math','art']
info = {'name':'jhon','age': 25 }
student_info(couses,info)
student_info(*couses,**info)

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year%4 == 0 and(year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    if not 1<= month <=12:
        return 'ivalid Mouth'
    if month ==2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2021,3))