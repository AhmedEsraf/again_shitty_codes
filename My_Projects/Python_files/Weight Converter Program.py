input_weight = float(input("Enter your weight: "))

# use \n to make the strings go to next line

type = input("Press L : 'Lbs to Kg'\notherwise,\nPress K : 'Kg to Lbs' : ")
if type == "L" or type == "l":
    weight = input_weight * 0.45
    print(f"Your weight is {weight} kilos")
elif type == "K" or type == "k":
    weight = input_weight * 2.204
    print(f"Your weight is {weight} lbs")
else:
    print("Invalid Input")

