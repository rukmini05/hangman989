import random
word_list=["apple","banana","berry","cherry","plum"]
word = random.choice(word_list)  
print(word_list)
print(word)
guess=input("emter single letter")
if len(guess)==1 and guess.isalpha:
    print("pass")
else:
    print("fail")
    