power =lambda base,exponent:base**exponent

def main():
    base=float(input("Enter base value "))
    exponent=float(input("Enter exponent value"))
    result=power(base,exponent)
    print(result)
    
main()