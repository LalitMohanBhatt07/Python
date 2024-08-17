def check(year):
    if(year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
    
def main():
    year=int(input("Enter a year: "))
    result =check(year)
    print(result)
    
main()