def concatenate(tupleOne,tupleTwo):
    concatenatedtuple=tupleOne+tupleTwo
    return concatenatedtuple

def main():
    tupleOne=(1,2,3)
    tupleTwo=(5,6,6)
    result=concatenate(tupleOne,tupleTwo)
    print(result)
    
main()