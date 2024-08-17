def findMiddleElement(s):
    length=len(s)
    
    #Check if the length of the string is odd
    if length%2!=0:
        middleIndex=length/2
        return s[middleIndex]
    else:
        return "Nothing"
    
    
def main():
    user_input=input("Enter a string")
    result=findMiddleElement(user_input)
    
    print("The middle element is : ",result)
    
    
main()