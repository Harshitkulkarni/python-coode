'''
Map()

map will accept only 2 parameter they are function and iterable object
map will return the iterator object
we need to convert the iterator object to whatevere we want like list tuples etc

map syntax :- map(function , iterable_object)


'''
def double(x):
    return x*2
l1= [1,2,3,4,5,6]
double_li = list(map(double,l1))
print(l1)
print(double_li)


l2 = [1,5,66,]
l2= list(map(float,l2))
print(l2)