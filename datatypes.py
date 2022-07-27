Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list
>>> l=[10,20,30,40,50]
>>> print(l)
[10, 20, 30, 40, 50]
>>> for x in l:
	print(x)

	
10
20
30
40
50
>>> print(l.append(60))
None
>>> print(l)
[10, 20, 30, 40, 50, 60]
>>> l.remove()

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    l.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> l.remove(60)
>>> print(l)
[10, 20, 30, 40, 50]
>>> # tupple
>>> t1=(10,20,30,40,50)
>>> print(t1)
(10, 20, 30, 40, 50)
>>> for x in t1:
	print(t1,end="")
	
SyntaxError: invalid syntax
>>> for x in t1:
	print(t1)

	
(10, 20, 30, 40, 50)
(10, 20, 30, 40, 50)
(10, 20, 30, 40, 50)
(10, 20, 30, 40, 50)
(10, 20, 30, 40, 50)
>>> for x in t1:
	print(x)

	
10
20
30
40
50
>>> li=list(t1)
>>> print(li)
[10, 20, 30, 40, 50]
>>> li.append(70)
>>> li.append(80)
>>> print(li)
[10, 20, 30, 40, 50, 70, 80]
>>> t=tupple(li)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t=tupple(li)
NameError: name 'tupple' is not defined
>>> t=tuple(li)
>>> print(t)
(10, 20, 30, 40, 50, 70, 80)
>>> for x in t:
	print(x)

	
10
20
30
40
50
70
80
>>> print(type(t))
<type 'tuple'>
>>> print(type(li))
<type 'list'>
>>> #SET
>>> s={10,20,30,40,'sarb','komal'}
>>> print(s)
set([40, 10, 'sarb', 20, 'komal', 30])
>>> for x in s(4):
	print(x)

	

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for x in s(4):
TypeError: 'set' object is not callable
>>> for x in s:
	print(x)

	
40
10
sarb
20
komal
30
>>> s.insert('jagdeep')

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.insert('jagdeep')
AttributeError: 'set' object has no attribute 'insert'
>>> s.append(39)

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s.append(39)
AttributeError: 'set' object has no attribute 'append'
>>> l2=list(s)
>>> l2.append('jk')
>>> l2.append('gurjeet')
>>> print(l2)
[40, 10, 'sarb', 20, 'komal', 30, 'jk', 'gurjeet']
>>> print(type(l2))
<type 'list'>
>>> s1=set(l2)
>>> print(s1)
set(['gurjeet', 40, 10, 'sarb', 20, 'komal', 'jk', 30])
>>> print(type(s1))
<type 'set'>
>>> f=frozenset(s2)

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    f=frozenset(s2)
NameError: name 's2' is not defined
>>> f=frozenset(s1)
>>> print(f)
frozenset([40, 10, 'gurjeet', 20, 'komal', 'jk', 30, 'sarb'])
>>> print(type(f))
<type 'frozenset'>
>>> d={'name':'sarbjeet','class':'btech','rollno':'4230','address':'raikot'}
>>> for x in d:
	print(x)

	
address
name
rollno
class
>>> print(d.keys)
<built-in method keys of dict object at 0x0000000002ECA8C8>
>>> print(d.key)

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(d.key)
AttributeError: 'dict' object has no attribute 'key'
>>> print(d.values())
['raikot', 'sarbjeet', '4230', 'btech']
>>> print(d.keys())
['address', 'name', 'rollno', 'class']
>>> d.append('distt':'ldh')
SyntaxError: invalid syntax
>>> d['name']='jagdeep'
>>> print(d)
{'address': 'raikot', 'name': 'jagdeep', 'rollno': '4230', 'class': 'btech'}
>>> #FUNCTIONS
>>> def sum(a,b):
	c=a+b
	return c
print("the sum is:",sum(10,20))
SyntaxError: invalid syntax
>>> def sum(a,b):
	c=a+b;
	return c;

>>> print(sum(10,20))
30
>>> print('the sum is:',sum(20,30))
('the sum is:', 50)
>>> def mul(a,b,c):
	m=a*b*c
	return m

>>> print("the multiply of three no.s is:",mul(10,20,30))
('the multiply of three no.s is:', 6000)
>>> 
