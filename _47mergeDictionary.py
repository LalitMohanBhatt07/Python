def merge(dic1,dic2):
    merged=dic1.copy()
    merged.update(dic2)
    return merged
    
dic1={'a':1,'b':2}
dic2={'b':'3','c':4}

result=merge(dic1,dic2)
print("Merged dictionary : ",result)