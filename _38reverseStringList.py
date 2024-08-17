numbers=[1,2,3,4,5]

reversedNumbers=list()

for i in numbers:
    reversedNumbers=[i]+reversedNumbers
    
print(reversedNumbers)