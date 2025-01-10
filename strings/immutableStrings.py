s1='kodnest'
s1.upper()
print(s1)
#strings are immutable thats y the output remains same
# for converting we need  to declare the reference variable

s2='kodnest'
s2=s2.upper()
print(s2)

s3 = 'k'
print(s1, id(s1))

s4= 'hello'
s5= 'world'
#accessing the specific word of the string
print(s4[0])
print(s4[-1])
#accessing the id(address) of the h in s4
print(('s4 id of the h',id(s4[0])))
print(('s4 id of o',id(s4[-1])))

print(('s5 id of the w',id(s5[0])))
print(('s5 id of o',id(s5[1])))
#python internally uses string interinig
#string interning is thr process of checking string intern pool before creating any new object
#when ever we want to create the  new object first python will internally  check weather the object is already present 
# if the object is already present  in string intern records then the address of the exsiting object is reused 