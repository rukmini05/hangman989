"""import random

def get_random_word_from_list(word_list):
    
    return random.choice(word_list)

def get_valid_letter_guess():
    
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def main():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    random_word = get_random_word_from_list(words)
    print(f"The random word is: {random_word}")  # For testing purposes

  
    valid_guess = get_valid_letter_guess()
        
    if valid_guess in random_word:  
        print(f"Good guess! {valid_guess} is in the word.")  
    else:
        print(f"Sorry, {valid_guess} is not in the word. Try again.") 

if __name__ == "__main__":
    main()"""


import random

def get_random_word_from_list(word_list):
    
    return random.choice(word_list)

def check_guess(guess, word):

    guess = guess.lower()  # Step 2
    if guess in word:  # Step 3
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):

    while True:
        guess = input("Guess a letter: ")  
        if len(guess) == 1 and guess.isalpha():  
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess, word) 

def main():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    random_word = get_random_word_from_list(words)
    print(f"The random word is: {random_word}")  

    ask_for_input(random_word)  

if __name__ == "__main__":
    main()