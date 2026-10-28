import random

def is_correct(guess_code, correct_code):
    return guess_code == correct_code
    
def generate_random_passcode():
    random_passcode = ""
    
    for i in range(4):
        random_digit = random.randint(0, 9)
        random_passcode += str(random_digit)
    return random_passcode

secret_passcode = generate_random_passcode()

def guess_every_possible_passcode(correct_code):
    num_guesses = 0
    for first_digit in range(10):
        for second_digit in range(10):
            for third_digit in range(10):
                for fourth_digit in range(10):
                    current_guess = "" + str(first_digit) + str(second_digit) + str(third_digit) + str(fourth_digit)
                    num_guesses += 1
                    if is_correct(current_guess, correct_code):
                        print("Correct passcode: " + str(current_guess))
                        print("It took " + str(num_guesses) + " guesses to find the correct passcode.")
                        return current_guess
    return ""
def is_correct(guess_code, correct_code):
    return guess_code == correct_code

def generate_random_passcode():
    random_passcode = ""
    for i in range(4):
        random_digit = random.randint(0, 9)
        random_passcode += str(random_digit)
    return random_passcode

secret_passcode = generate_random_passcode()
correct_passcode = guess_every_possible_passcode(secret_passcode)
