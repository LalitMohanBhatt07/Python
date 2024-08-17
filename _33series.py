import pandas as pd

# additon
def performOperation(series1,series2):
    addition=series1+series2
    
    substraction=series1-series2
    
    multiplication=series1*series2
    
    division=series1/series2
    
    # display result
    print("Series 1 : ")
    print(series1)
    
    print("Series 2")
    print(series2)
    
    print("Additon of series : ")
    print(addition)
    
    print("Substractio : ")
    print(substraction)
    
    print("multiplication : ")
    print(multiplication)
    
    print("Division")
    print(division)
    
def main():
    series1=pd.Series([10,20,30,40,50])
    series2=pd.Series([5,4,3,2,1])
    
    performOperation(series1,series2)
    
    
main()