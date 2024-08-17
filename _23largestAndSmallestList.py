def findLargestAndSmallest(numbers):
    largest=numbers[0]
    smallest=numbers[0]
    
    for number in numbers:
        if number>largest:
            largest=number
        else:
            smallest=number
    print("Smallest number is : ",smallest)
    print("Largest number is :",largest)


def main():
    inputList=[]
    
    for i in range(5):
        number=int(input("Enter number:"))
        inputList.append(number)
        
    findLargestAndSmallest(inputList)
    
    
main()