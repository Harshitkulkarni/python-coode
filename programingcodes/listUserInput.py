'''
list user input in 1st way

'''
'''
l1 = []
num = int(input('enter count: '))
for i in range(num):
    ele = int(input(f'enter the elements {i}  '))
    l1.append(ele)

print(l1)
'''

'''
output:
enter count: 5
enter the elements 0  100
enter the elements 1  200
enter the elements 2  300
enter the elements 3  400
enter the elements 4  500
[100, 200, 300, 400, 500]
'''
#in 2nd way
'''
list user input in second way
'''
'''
li = input('enter the space separated elements ')
print(li, type(li))
li = li.split()
print(li)
li = list(map(int,li))
print(li)
'''
'''
tup =tuple(map(int,input('enter the space seprated elements ').split()))
print(tup)

'''
