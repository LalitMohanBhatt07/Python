import _17modulesPython


def main():
    print("Select Operation")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    
    choice=int(input("Enter your choice: "))
    
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))
    
    if choice==1:
        print("Result : ",_17modulesPython.add(num1,num2))
    
    elif choice==2:
        print("Result : ",_17modulesPython.subs(num1,num2))
        
    elif choice==3:
        print("Result",_17modulesPython.mul(num1,num2))
        
    elif choice==4:
        print("Result : ",_17modulesPython.division(num1,num2))
        
        
main()