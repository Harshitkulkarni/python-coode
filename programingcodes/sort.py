'''
sort() and sorted()

'''

l1 =[10,5,3,20]
l1.sort()# by default the sort is assending order
print(l1)

# to get descending order
l1.sort(reverse=True)
print(l1)

#sorted()
#create the new copy where as sort will modify in the original list
l2=[100,200,300,400]
sorted_l2 = sorted(l2)
print(sorted_l2)