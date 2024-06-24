
import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_ '] * len(self.word)
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = [ ]
    
    def check_guess(self, guess):
        guess.lower()
      
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')

            for i, letter in enumerate(self.word):
                if letter==guess:
                    self.word_guessed[i]=guess

            print(self.word_guessed)  

            self.num_letters -= 1

        else:
            self.num_lives -= 1    
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')
    
    def ask_for_input(self):
        while True:
            guess = input('Enter Guess a letter: ')

            if (guess.isalpha() == False) or len(guess) != 1:
                print ('Invalid letter. Please enter a single alphabetical character.')

            elif guess in self.list_of_guesses:
                print(f'You already tried that letter!')
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
                break
    

def play_game():
  
    
    word_list = ['apple', 'banana', 'orange', 'strawberry', 'mango', 'watermelon']
    game=Hangman(word_list)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0 :
             game.ask_for_input()    
        else: 
            print('Congratulations! You have won!')
            break
              
play_game()
