import random

names = ['qasem', 'hassan', 'ali', 'morteza', 'nirvana', 'mostafa']
r = random.choice(names)
guess_list = ["-"] * len(r)
guess_count = len(r)
print(guess_list)

while True:


    user_guess = input("Enter a letter: \n")
    
    if user_guess in guess_list:
        print("You've already guessed that letter.")
        continue

    if not user_guess.isalpha():
        print("Please enter a valid letter.")
        continue
    if len(user_guess) != 1:
        print("Please enter only one letter.")
        continue
    if user_guess in r:
        for i, latter in enumerate(r):
            if user_guess == latter:
                guess_list[i] = user_guess
        print(guess_list)
    else:
        print(f"Your guess was incorrect. You have {guess_count} attempts left.")
        guess_count -= 1
    if not "-" in guess_list:
        print("Congratulations! You've guessed the word.")
         
        again = input("Do you want to play again? (Y/N)").lower()
        if again != "y":
            print("Thank you for playing!")
            break
        
        if again == "y":
            r = random.choice(names)
            guess_list = ["-"] * len(r)
            guess_count = len(r)
            print(guess_list)

    if guess_count == 0:
        print("Sorry, you lost.")
        again = input("Do you want to play again? (Y/N)").lower()
        if again != "y":
            print("Thank you for playing!")
            exit()