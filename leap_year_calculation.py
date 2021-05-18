# Leap year coding challenge

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print(f"still checking if this year {year} is a leap year")
    if year % 100 == 0:
        print(f"Still checking ...")
        if year % 400 == 0:
            print(f"This year {year} is a Leap year")
        else:
            print(f"This year {year} is Not a Leap year")
    else:
        print(f"This year {year} is a Leap year")
else:
    print(f"This year {year} is Not a Leap year")

