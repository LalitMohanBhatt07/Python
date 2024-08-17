import pandas as pd

def convertSeriesToList():
    #create a panda series
    data=pd.Series([10,20,30,40,50])
    
    #convet panda seriews into python list
    dataList=data.tolist()
    print("dta",data)
    
    print("list: ",dataList)
    
    
def main():
    convertSeriesToList()
    
main()