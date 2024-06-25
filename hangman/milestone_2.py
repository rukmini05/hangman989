"""import random
word_list=["apple","banana","berry","cherry","plum"]
word = random.choice(word_list)  
print(word_list)
print(word)
guess=input("emter single letter")
if len(guess)==1 and guess.isalpha:
    print("pass")
else:
    print("Oops! That is not a valid input") """
    
import random

def get_random_word_from_list(word_list):
    """Select and return a random word from the provided list."""
    return random.choice(word_list)

def main():
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    vegetables = ["carrot", "broccoli", "asparagus", "cauliflower", "spinach"]

    random_fruit = get_random_word_from_list(fruits)
    random_vegetable = get_random_word_from_list(vegetables)

    print(f"Random Fruit: {random_fruit}")
    print(f"Random Vegetable: {random_vegetable}")

if __name__ == "__main__":
    main()