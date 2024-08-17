def main():
    with open('myFile.txt','w') as f:
        for i in range(1,3):
            line=input("Enter line :")
            f.write(line+"\n")
            
main()