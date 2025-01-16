'''what is list slicing ?
is used to create sublist from main list'''
#syntax == list_name[start:end-1:steps]
li1= [10,20,30,40,50]
subli=li1[0:4:1]
print(subli)

subli2 = li1[1::]
print(subli2)

subli3 = li1[::2]
print(subli3)

reverse_list = li1[::-1]
print(reverse_list)


subli4=li1[-1::]#last element will be printed
print(subli4)