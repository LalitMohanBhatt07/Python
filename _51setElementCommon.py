def haveCommonElement(set1,set2):
    return len(set1.intersection(set2))>0


set1={1,2,3,4,5}
set2={4,5,6,7,8}
if haveCommonElement(set1,set2):
    print("the sets have common elements ")
else:
    print("There is no common elements ")