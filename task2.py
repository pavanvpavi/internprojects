import random

def main():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))

            if guess < 1 or guess > 20:
                print("Please guess a number between 1 and 20.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    main()
