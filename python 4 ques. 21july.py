#1) Given l1 = ['m' , 'n'] and n=3 show that output ['m1', 'm2', 'm3', 'n1', 'n2', 'n3']
l1 = ['m','n']
n=3
new_list = ['{}{}'.format(x,y) for y in range(1, n+1) for x in l1]
print(new_list)
#2) [[4,5,3], [6,3,2],[6,9,1]]    output = [12, 11, 16]
list = [[4, 5, 3], [6, 3, 2], [6, 9, 1]]
res = [sum(x) for x in list]
print(res)
#3) Remove the duplicate number [1,2,3,0,1,1,4,5,2,3]
list1 = ["1","2","3","0","1","1","4","5","2","3"]
list1 = list(dict.fromkeys(list1))
print(list1)
#4) 1200 to 3000 numbers are divisible by 4 and 8 but not divisible by 6 
#first method
lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if((i%4==0) & (i%8==0) & (i%6!=0)):
              print (i)

#second method
for i in range(1200, 3000): 
	if i%4==0 and i%8==0 and i%6!=0:
            print(i)
