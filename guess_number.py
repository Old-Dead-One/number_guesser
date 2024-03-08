""" Divide the possible range in half. """

def calc_guess(min_value, max_value):
    return (min_value + max_value) // 2

""" Give the computer a hint. """

def user_hint(guess):
    print(f"Is your number {guess}?")
    hint = input("Enter 'h' if my guess is too high, 'l' if too low, or 'c' if correct: ")
    return hint

""" Update the possible range."""

def update_range(hint, guess, min_value, max_value):
    if hint == "h":
        max_value = guess - 1
    elif hint == "l":
        min_value = guess +1
    return min_value, max_value

""" Start Guesser """

def start_game():
    min_value = 1
    max_value = 100
    hint = ""

    while hint != "c":
        guess = calc_guess(min_value, max_value)
        hint = user_hint(guess)
        if hint not in ["h", "l", "c"]:
            print("Please enter 'h', 'l', or 'c'.")
        
        elif hint == "c":
            print(f"Your number is {guess}! And you thought you could outsmart me!")
            break
        min_value, max_value = update_range(hint, guess, min_value, max_value)


def main():
    start_game()

if __name__ == "__main__":
    main()
