t1=(10,20,30,40,50,60)
print(len(t1))
print(max(t1))
print(min(t1))
print('convert tuple into list')
l1=list(t1)
print(l1)
print('convert list into tuple')
t2=tuple(l1)
print(t2)
print('concatinating 2 tuples')
t1=t1+t2
print(t1)
del t2;
print('t2 tuple deleted')