while True:

    guess=input("enter single letteer")
    if guess.isalpha() and len(guess)==1 :
        print("pass")
        break
    else:
        print("invalid")