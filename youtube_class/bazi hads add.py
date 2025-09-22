import random



def welcome ():
    print("Welcome to this funny game ")
    print("I will choose a number between 1 , 20 and")
    print("you have to guess it....")
    print("go go go....")
    print()
    
    
def finish(number, count):
    print("Good game ")
    print(f"my number was {number} and you found it in {count} guesses./n")
    answer = input("Do you want to play again? (Y/N): ")
    return answer.upper() == "Y"


def win(computer_number, guess):
    return computer_number == guess 

def answer(computer , user):
    if computer > user:
        return "My number is larger"
    elif computer < user :
        return "ohh .. you went so large! mine is smaller"
    
    return"Wow! you won! Good Guess!"

        
        
def get_a_guess():
    while True:
        try:
            ans= int(input("what is your guess (1-20) ?"))
            if 1 <= ans <= 20 :
                return ans
            else :
                print("Please Enter a number between 1 and 20 ")
        except ValueError:
            print("Please enter a valid number !")
            
            
best_score = None             
 
    
welcome()
continue_playing = True
while continue_playing:
    computer_number = random.randint(1 , 20)
    guess = 0
    count = 0
    
    while not win(computer_number, guess):
        guess = get_a_guess()
        print(answer(computer_number, guess))
        count += 1
        
        
    if best_score is None or count < best_score:
        best_score = count
        print("New record ! You guessed it in fewer tries than ever!")
    else :
        print(f"Your best score so far is {best_score} guesses")    
        
        
    continue_playing = finish(computer_number, count)
    


