s1={1,2,3,4,5}
print(s1)
s2={4,5,6,7,8}
print(s2)
s2.add(9)
print(s2)
s2.copy()
s2.discard(9)
print(s2)
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.union(s2))
print(s1.symmetric_difference(s2))
s1.remove(1)
print(s1)
s1.pop()
print(s1)
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
