def main():
    with open("intern.txt","w") as file:
        line=input("Write a single line of text : ")
        
        file.write(line)
        
        print("Text has been writen to intern.txt")
        
        
main()