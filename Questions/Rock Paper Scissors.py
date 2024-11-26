import random

ver1 = "Rock"
ver2 = "Paper"
ver3 = "Scissors"

print(" Type\n R for Rock \n P for Paper \n S for Scissors \n")

user_choice = input('>>').lower()


computer_choice = random.choice([ver1,ver2,ver3])

if user_choice == 'r':
    user_choice = "Rock"
elif user_choice == 'p':
    user_choice = "Paper"
elif user_choice == 's':
    user_choice = "Scissors"
else:
    print('You typed something wrong')
    exit()

print('You Chose '+ user_choice+ '.\n')

print("Computer chose "+ computer_choice + '.\n')


if user_choice == "Rock" and computer_choice == "Paper":
    print('You win!!')
elif user_choice == "Paper" and computer_choice == "Rock":
    print('You lose!!')
elif user_choice == "Scissors" and computer_choice == "Paper":
    print('You win!!')
elif user_choice == "Paper" and computer_choice == "Scissors":
    print('You lose!!')
elif user_choice == "Rock" and computer_choice == "Scissors":
    print('You win!!')
elif user_choice == "Scissors" and computer_choice == "Rock":
    print('You lose!!')
elif user_choice == computer_choice:
    print("It's a tie!!")
else:
    print('Invalid Logic')