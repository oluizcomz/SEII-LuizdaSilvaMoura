# work with condicional
if True:
    print('Condicional was True')
#language ='Python'
language ='Java'
if language =='Python':
        print('Linguage is Phiton')
elif language =='Java':
    print('Linguage is Java')
elif language =='JavaScript':
    print('Linguage is JavaScript')
else:
    print ('No match')
#and = &&
#or = ||
#not = !=
user = 'Admin'
logged_in = True
if user =='Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad crad')
#logged_in = False
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

#is compara id(possiçao da memoria)
a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))

print(a is b)
b = a
print(a is b)  
condition = 0# or '' or [] or {} contendo estruturas nulas
if condition:
        print('Evalueted to true')
else:
    print('Evaluated to False')

condition = 'Test'# extruturas nao nulas
if condition:
        print('Evalueted to True')
else:
    print('Evaluated to False')