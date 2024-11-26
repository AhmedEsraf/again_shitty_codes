import random

def play_game():
    random_number = random.randint(1, 100)
    secret_number = random_number
    i = 0
    tries = 1

    print("\nThe Secret number is between 1 and 100.\nGuess the secret number in 7 tries to win.\n")

    while i < 7:
        guess = int(input(f"Guess the secret number [try number: {tries}] ---> "))
        i += 1
        tries += 1
        if guess == secret_number:
            print("Congrats! You win!")
            return True
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
    
    if i == 7 and guess != secret_number:
        print(f"Sorry! You lose! The secret number was {secret_number}.")
        return False

def retry_function():
    while True:
        if not play_game():
            break
        
        retry = input("Do you want to play again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Start the game
retry_function()
