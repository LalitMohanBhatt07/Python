def count_character(fileName):
    with open(fileName,'r') as merge:
        content=merge.read()
        
        uppercase_count=0
        lowercase_count=0
        digit_count=0
        
        for char in content:
            if char.isupper():
                uppercase_count+=1
            elif char.islower():
                lowercase_count+=1
            elif char.isdigit():
                digit_count+=1
                
        print("Total number of uppercase letters ",uppercase_count)
        print("Total number of lowecase letters : ",lowercase_count)
        print("Total number of digits : ",digit_count)
        
def main():
    fileName='merge.txt'
    count_character(fileName)
    
main()