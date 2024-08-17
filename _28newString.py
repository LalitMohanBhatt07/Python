def swapFirstLastCharacter(s):
    if len(s)<=1:
        return s
    
    newString=s[-1]+s[1:-1]+s[0]
    return newString

def main():
    userInput=input("Enter a string : ")
    result=swapFirstLastCharacter(userInput)
    
    print("new string is : ",result)
    
main()