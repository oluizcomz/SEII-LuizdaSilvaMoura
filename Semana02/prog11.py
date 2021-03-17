#work with file
f = open('test.txt','r')
print('name file:',f.name)
f.close()
print('\n read() \n')
with open('test.txt','r') as g:
    print(g.read())

print('\n read line \n')
with open('test.txt','r') as h:
    for line in h:
        print(line, end = ' ')

print('\n read(caracter)\n')
with open('test.txt','r') as i:
    print('\n',i.read(20))
    print('\n',i.read(20))
    print(i.tell())
    i.seek(0)
    print('\n',i.read(20))

with open('test2.txt','w') as j:
    j.write('Test')
    j.seek(0)
    j.write('R')

with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

with open('logo.png','rb') as rf:
    with open('logo_copy.png','wb') as wf:
        for line in rf:
            wf.write(line)
