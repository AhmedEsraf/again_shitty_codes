# If or else statements and elifs

is_cold = True
is_hot = False

if is_cold:
    print("Is column cold!")
elif is_hot : # use elif to extend conditions
    print("It's shining hot!")
else:
    print("Just an Average day.")

print('Have a nice day!')

# Exercise

''' Price of a house is $1M.
If buyer has good credit,
    they need to put down 10%.
Otherwise,
    hey need to put down 20%.
Print the down payment. '''

has_good_credit = True
price = 1000000

if has_good_credit:
    down_payment = int(price * 0.1)

else:
    down_payment = int(price * 0.2)

print('Your down payment is $'+ str(down_payment))

# or

print(f'Your down payment is ${down_payment}')