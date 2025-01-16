l1 = [1,2,3,4,5,]#write program to square the elements
sq_li=[]
for i in l1:
    sq_li.append(i**2)
print(sq_li)

'''
list comprehension 
syntax for only one condition  == [expresion for i in iterable_object condition ]
syntax for mutliple  condition  == [expresion for i in iterable_object condition ]
'''
l2=[1,2,3,4,5,6,7,8,9]
duplicate_l2=[i  for i in l2]
print(duplicate_l2)

square_list=[i**2 for i in l2]
print(square_list)

even=[i for i in l2 if i%2==0]
print(even)

#for both if and else we use 

even_or_odd=['even' if i%2==0 else 'odd' for i in l2]
print(even_or_odd)

#nested for loops in list comprehensions
l3=[[10,20],[30,40],[50,60]]
print(l3)#[[10, 20], [30, 40], [50, 60]]
new_l3=[ele for i in l3 for ele in i]
print(new_l3)#[10, 20, 30, 40, 50, 60]

