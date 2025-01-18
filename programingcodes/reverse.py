'''
reverse 
onject.revrese() will reverse the original object.
'''

li=[10,20,30,40,50]
li.reverse()
print(li)
#reversed(object) will return an iterable object to get output we need to convert the iterable object to list
#by list(reversed(object))
l2=[11,6,8,6,4,]
reverse_l2=list(reversed(l2))
print(l2)
print(reverse_l2)

l3 = [1,5,6,9]
new_reverse_l3 = list(reversed(l3)) #creating new reverse list
l3.reverse()# reversing the original list