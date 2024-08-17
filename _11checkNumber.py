def check(num):
    if(num>=100):
        if(num%2==0):
            return "Number is greater than 100 and is Even"
        else:
            return "Number is greater than 100 and is Odd"
    else:
        return "Less than 100"
    
def main():
    num=int(input("Enter a number: "))
    result=check(num)
    print(result)
    

main()