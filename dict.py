'''
dict is muteable
'''
d1= {
        'name':'hat',
        'age':24,
        'phone':235564
    }
print(d1,type(d1))
#in dict we cannot store duplicate keys.
#in dict we can store values
d1['name'] = 'bat' # replace the name
print(d1)

marks = {'science':85,'maths':85}#Dublicate value are allowed

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)