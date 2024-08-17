def factorial(n):
    if n<0:
        return "Factorial is not defined for negative number"
    elif n==0 or n==1:
        return 1
    else:
        result=1
        for i in range(2,n+1):
            result=result*i;
    return result;
        
def main():
    userInput=int(input("Enter a number of find its factorial : "))
    result=factorial(userInput)
    print("Factoraial of number is : ",result)
    
    
main()