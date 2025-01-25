while True:
    year=int(input("Enter the year"))
    if year%4 == 0 and year%400 != 0:
        print("The given Year is Leap year")
    else:
        print("The given year is not leap year")