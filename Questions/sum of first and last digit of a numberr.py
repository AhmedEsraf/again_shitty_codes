def sum_of_first_n_last_digit():
    
    number =  input("Type Your Number:")
    number_string = str(number)
    digits = []
    for i in number_string:
        digits.append(i)
    
    summation = int(digits[0]) + int(digits[-1])
    print("The sum of first and last digit of your number:", summation)
    return 0


sum_of_first_n_last_digit()


def sum_without_list():
    number =  input("Type Your Number:")
    number_string = str(number)
    first_digit = int(number[0])
    last_digit = int(number[-1])
    summ = first_digit + last_digit
    print("The sum of first and last digit of your number:", summ)
    return 0

sum_without_list()
