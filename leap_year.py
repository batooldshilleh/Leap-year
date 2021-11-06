year = int (input("enter the year"))
if year % 4 == 0 :
    if year % 100 ==0 :
        if year % 400 == 0 :
            print (f"{year} is leap")
        else: print(f"{year} not leap")
    else: print(f"{year} leap")
else: print(f"{year} not leap")
