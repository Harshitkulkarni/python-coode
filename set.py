'''
in sets we can store both homogeneous an thetrogenous data
set is an unordered collection of the data
set does not support indexing of the data
in sets we cannot store dublicate value
sets are mutable
'''
s1 = {10,True,'Kodnest',10,25,55.5} #{True, 55.5, 25, 10, 'Kodnest'} <class 'set'>
print(s1,type(s1))
#print(s1[0]) gives an error

#add() method is used to add elements to the set
s1.add(500)
print(s1)

#remove() method is used to remove the elements
s1.remove(55.5)
print(s1)

#pop() without index will delete and return one element
s1.pop()
print(s1)

del s1 #complete set will be delete