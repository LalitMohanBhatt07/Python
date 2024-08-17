def keyExist(dictionary,key):
    return key in dictionary

myDict={'a':10,'b':20,'c':30}

key='b'

if keyExist(myDict,key):
    print("key",key,"Exist n the dictionary ")
else:
    print("key",key,"does not exist in the dictionary")