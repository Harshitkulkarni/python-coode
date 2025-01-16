'''
list():
list () is accepting parameters as only iterable object
'''

l1= list("kodnest")
print(l1)

l2=list((10,20,30))
print(l2)

l3=list({100,200,300})
print(l3)

l4=list({'name':'hat','age':54})
print(l4)

l5=list(range(10,20))
print(l5)

print("--------------------------------------------------------------")

'''
tuples():
'''
tup1=tuple([10,20,30])
print(tup1)
tup2=tuple({100,200,300})
print(tup2)
tup3=tuple(range(10,21))
print(tup3)
tup4=tuple('Kodnest')
print(tup4)
tup5=tuple({'name':'hat','age':54})
print(tup5)

print("------------------------------------------------------------------------------")

'''
sets():
'''

s1= set([10,20,30])
print(s1)

print("-----------------------------------------------------------------------------")

'''
dict
'''
d1 = dict([['name','hat'],['age',25]])
print(d1)