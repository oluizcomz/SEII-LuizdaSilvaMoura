#work with variable global and local
x = 'global'
def test(z):
    y ='local'
    print(y)
    print(x)
    print(z)

test('local')
print(x)
def func():
    k = 'local para func'
    def arrowfunc():
        #nonlocal k #pega a de maior nivek analogo a this.
        k = 'local para arrow'
        print(k)
    arrowfunc()
    print(k)
func()
