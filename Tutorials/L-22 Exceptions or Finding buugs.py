try:
    age = int(input("Enter your age: "))
    income = int(input("Enter your income: "))
    risk = income / age
    print("Your risk is:", risk)
except ValueError:
    print("Please enter an integer")
except ZeroDivisionError:
    print("Please don't enter zero")

# this basically means if the program gives ValueError then it will print that messag3e
# this prevents crashing the program
# this error is called exception
# exit code 0 means program succesfully ran and exit code 1 means code crashed