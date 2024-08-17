def sum(n):
     i=1
     sum=0
     while(i<=n):
         sum=sum+i
         i=i+1
     return sum
     
     
def main():
    num=int(input("Enter value of n"))
    result=sum(num)
    print(result)
    
    
main()
    

    