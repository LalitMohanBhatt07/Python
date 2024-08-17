def printEven(n):
    i=2;
    while i<=n:
        print(i)
        i=i+2
        
def main():
    n=int(input("Enter value of n"))
    printEven(n)
    
main()