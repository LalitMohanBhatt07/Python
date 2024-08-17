import math
def compute(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

def main():
    x1 = float(input("Enter x1: "))
    y1= float (input("Enter y1: "))
    x2 = float(input("Enter x1: "))
    y2= float (input("Enter y1: "))
    
    distance=compute(x1,y1,x2,y2)
    print("the distance beween the points ({},{}) and ({},{}) is {}".format(x1,y2,x2,y2,distance))
    
    
main()