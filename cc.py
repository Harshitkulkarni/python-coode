'''

'''

def checkAge(age):
    if(age<18):
        print('child')
    elif(age>65 and age<65):
        print("Adult")
    elif(age>65 ):
        print("senior citizen")
checkAge(int(input('enter the age')))        

