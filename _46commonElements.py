def commonElements(tupleOne,tupleTwo):
    for element in tupleOne:
        if element in tupleTwo:
            return True,
    return False

    
tupleOne=(1,2,3,4,6)
tupleTwo=(6,7,8,9,10)   
result=commonElements(tupleOne,tupleTwo)
print(result)
  