import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    while True:
        user_input = int(input('Guess the secret number? '))
        try:
            num = int(user_input)
            if 1 <= num <= 10:
                return num # Valid integer within range
            else:
                print(f"Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    #Create count variable to count number of guesses
    guess_count = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        #Once a guess is made, add 1 to the count.
        guess_count+=1

        if result == correct:
            break

    print('Thanks for playing the game!')
    #Prints the amount of tries to get the right number!
    print(f'It took you {guess_count} tries to get the right answer!')


if __name__ == '__main__':
    main()
