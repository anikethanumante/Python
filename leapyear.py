#leap year code

print("Please enter a year: ")

year = int(input())

""" a year is leap year if it is divisible by 4.
however,centuries are not leap years, although tey are divisible by 4.
But centuries that are divided into 400 are still leap year."""

#If reminder of division by 4 is not zero,then year is not divisible by 4,therefor it is usual.

if year % 4 != 0:
    print("Usual year..!!")
elif year % 100 == 0:
    if year % 400 == 0:
        print("year is leap year..!!")
    else:
        print("Usual year..!!")
else:
    print("Year is leap year..!!")
