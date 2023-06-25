def Leap_year(year):
    if (year%4)==0:
        if (year%100)==0:
            if (year%400)==0:
                print("Leap Year")
            else:
                print("Not Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not Leap Year")

year=int(input("Enter a year: "))
Leap_year(year)

Output
Enter a year: 2024
Leap Year

