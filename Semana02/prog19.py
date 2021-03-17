#classe
li = [-9,1,8,2,7,3,6,4,5]
s_li = sorted(li)#(li,reverse=True)
#s_li = sorted(li,key =abs)
print('li ordenado \t',s_li)
print('li: \t',li)
li.sort()#(reverse=True)
print('li: \t',li)
di = {'name':'coret','job':'programming','age': None,'os':'Mac'}
s_di = sorted(di)
print('Dict:\t',s_di)

class Employee():
    #contrutor
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    #'metodo nativo'
    def __repr__(self):
        return '({},{},${})'.format( self.name , self.age , self.salary)

def e_sort(emp):
    return emp.name
e1 = Employee('Carl',37, 7000)
e2 = Employee('Sarah',29, 8000)
e3 = Employee('jhon',30, 9000)
employees = [e1,e2,e3]
s_employees = sorted(employees,key = e_sort)
print(s_employees)
print(e1)

