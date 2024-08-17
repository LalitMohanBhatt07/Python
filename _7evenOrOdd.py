def check(number):
    if number%2==0:
        return "even"
    else:
        return 'odd'
    
    
def main():
    number=int(input("Enter a number to check :"))
    result=check(number)
    print("The given number {} is {}".format(number,result))
    
main()