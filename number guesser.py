import random

lower_bound = 1
upper_bound = 10
max_attempts = 3

secret_number = random.randint(lower_bound, upper_bound) #generates a random number that is in the range.

def get_guess():
    while True:
        try:
            guess = int(input(f"guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("invalid input. Please enter a number within the range")
        except ValueError:
            print("Invaid input. Please enter a valid number")

#validating guess
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "too low"
    else:
        return "too high"

 #tracking the number of plays
def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "correct":
            print (f"congratulations! you guessed the secret number: {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result} try again!")

    if not won:
        print(f"sorry, you ran out of attempts, the secret number is {secret_number}")

if __name__== "__main__":
    print("welcome to the number guessing game")
    play_game()