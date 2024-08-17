import sys
def main():
    if len(sys.argv)!=3:
        print("Please provide exactely two numbers as command line arguemtn");
    else:
        num1=int(sys.argv[1])
        num2=int(sys.argv[2])
        
        result=num1+num2
        print("the result is ",result)
        
main()