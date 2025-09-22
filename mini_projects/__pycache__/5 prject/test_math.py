import random
import time


def question():
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    op_lis = ['+', '-', '*']
    sel_op = random.choice(op_lis)

    print(f"{a} {sel_op} {b} = ?")
    if sel_op == '-':
        return a - b
    elif sel_op == '+':
        return a + b
    else:
        return a * b
question_limit = 5
question_gen = 0
scorre = 0
while question_gen < question_limit:
    result = str(question())
    start_time = time.time()
    user_asnwe = input("Enter your answer").strip()
    end_time = time.time()
    dif_time = end_time - start_time
    if dif_time > 10 :
        print("your time is over ")
        break
    else:
        dif_time = 0
    if user_asnwe == result :
        scorre += 1
        print(f"Correct ! your scorre is {scorre}")
    else :
        print("Wrong!")
    question_gen += 1
    
    if question_gen == question_limit :
        print("Game Over.")
        again =input("Do you Want paly again? (Y/N)\n").strip().lower()
        if again == "y":
            question_gen = 0
            scorre = 0
        elif again == 'n':
            print("thanks for your playing")
            break
        