def check(char):
    if char.isslower():
        return 'LowerCase'
    elif char.isupper():
        return 'Uppercase'
    else:
        return "Not and Alphabet"
    

def main():
    char=input("Enter a character : ")
    result=check(char)
    print(result)
    
    
main()