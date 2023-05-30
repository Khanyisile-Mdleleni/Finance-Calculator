import math
def simple_interest(principal, rate, time):
    return principal * (1 + rate * time)

def compound_interest(principal, rate, time):
    return principal * math.pow((1 + rate), time)

def bond_calculator(principal, rate, time):
    interest = rate * principal
    x = (interest * time) / (1 - math.pow((1 + interest), -time))
    return x

# main menu
def show_menu():
    print("Welcome to the Bond and Investment Calculator!")
    print("Please select the calculator you want to use:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Bond Calculator")
    print("Q. Quit")

# user's choice
def get_user_choice():
    choice = input("Enter your choice: ").strip().lower()
    return choice

def validate_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_float_input(prompt):
    while True:
        value = input(prompt)
        if validate_float(value):
            return float(value)
        print("Invalid input. Please enter a valid number.")

def investment_calculator():
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1" or choice.startswith("simple"):
            principal = get_float_input("Enter the principal amount: ")
            rate = get_float_input("Enter the interest rate: ")
            time = get_float_input("Enter the time period (in years): ")
            result = simple_interest(principal, rate, time)
            print("Simple Interest: ", result)

        elif choice == "2" or choice.startswith("compound"):
            principal = get_float_input("Enter the principal amount: ")
            rate = get_float_input("Enter the interest rate: ")
            time = get_float_input("Enter the time period (in years): ")
            result = compound_interest(principal, rate, time)
            print("Compound Interest: ", result)

        elif choice == "3" or choice.startswith("bond"):
            principal = get_float_input("Enter the principal amount: ")
            rate = get_float_input("Enter the interest rate: ")
            time = get_float_input("Enter the time period (in years): ")
            result = bond_calculator(principal, rate, time)
            print("Bond Calculator: ", result)

        elif choice.startswith("q"):
            print("Thank you for using our Bond and Investment Calculator!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

investment_calculator()







