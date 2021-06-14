print("\n1 a)")
u = 1 #u(k = 0) = 1
for n in range(1,21):
    print(u)
    u = u +2#u(k) = u(k-1)+2

print("\n1 b)")
u = 0 
for n in range(1,21):
    u = u +n #u(k) = u(k-1)+n
    print(u)

print("\n1 c)")
u = 0 
for n in range(1,21):
    u = n*n #u(k) = u(k-1)+n
    print(u)


