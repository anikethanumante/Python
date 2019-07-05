
#Calculator program
#This is command line calculator program which have functinalities of addition,
#substraction,multiplication and division.
#If entered incorrect input it promts to try again functionality.

def add():
    """ addition function to add two numbers."""
    return round(num1+num2)

def sub():
    """ substraction function to substract two numbers."""
    return round(num1-num2)

def mul():
    """ multiplication function to multiply two numbers."""
    return round(num1*num2)

def div():
    """ division function to divide two numbers."""
    return round(num1/num2)

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
print("What operation you want to perform :")
print("1.addition")
print("2.substraction")
print("3.mutiplication")
print("4.division")

yes = 1
no = 0
while True:
    choice = input("Please enter your choice(1/2/3/4):")

    if choice == "1":
        print(num1, "+", num2, "=", add())
    elif choice == "2":
        print(num1, "-", num2, "=", sub())
    elif choice == "3":
        print(num1, "*", num2, "=", mul())
    elif choice == "4":
        print(num1, "/", num2, "=", div())
    else:
        print("Invalif input. Try again.")
    option = input("want to try again? (y/n) ")
    if option == 'n':
        print("Good Bye..!!")
        break


