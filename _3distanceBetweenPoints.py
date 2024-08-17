import math
def computeDistance(x1,y1,x2,y2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

result=computeDistance(2,1,4,8)
print(result)