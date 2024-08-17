def count(tuple,element):
    count=0;
    for item in tuple:
        if item==element:
            count+=1
    return count

def main():
    tuple=(1,2,3,1,4,1,65)
    
    result=count(tuple,1)
    print(result)
    
main()