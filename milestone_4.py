import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list  # List of possible words
        self.word = random.choice(word_list)  # Randomly select a word from the list
        self.word_guessed = ['_' for _ in self.word]  # List of underscores representing unguessed letters
        self.num_letters = len(set(self.word))  # Count of unique letters in the word
        self.num_lives = num_lives  # Number of lives the player has
        self.list_of_guesses = []  # List to track guessed letters

# Test the Hangman class
def main():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    hangman_game = Hangman(words)
    print("Word to guess:", hangman_game.word)
    print("Word guessed so far:", hangman_game.word_guessed)
    print("Number of unique letters:", hangman_game.num_letters)
    print("Number of lives:", hangman_game.num_lives)
    print("List of guesses:", hangman_game.list_of_guesses)

if __name__ == "__main__":
    main()