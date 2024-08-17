def findIndex(tuple,element):
    for i in range(len(tuple)):
        if tuple[i] == element:
            return i
    return -1

def main():
    tuple=(10,20,40,30,50)
    result=findIndex(tuple,10)
    print(result)
    
    
main()