import random


def number_guess_game():
    number = random.randint(1, 100)
    guesses = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Your guess: "))
        guesses += 1

        if guess < number:
            print("Too low! Try higher.")
        elif guess > number:
            print("Too high! Try lower.")
        else:
            print(f"✓ Correct! You guessed it in {guesses} guesses.")
            break


number_guess_game()
