print('lists datatype')
l1=[10,20,50,30,60,70]
l2=[1,2,3,4,5,6]
l1.append(40)
print(l1)
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.remove(20)
print(l1)
l1.pop()
print(l1)
l1.extend(l2)
print(l1)

print('printing list using loops')
for x in range(len(l2)):
    print(l2[x])
