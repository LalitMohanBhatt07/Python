list=[]

for i in range(1,6):
    mark=int(input("Enter marks : "))
    list.append(mark)
    
average=sum(list)/len(list)
print(average)