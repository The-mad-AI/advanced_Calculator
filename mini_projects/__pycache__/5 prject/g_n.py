import random
import os
from unittest.mock import patch, MagicMock

def load_best_record(record_file="record.txt"):
    if os.path.exists(record_file):
        with open(record_file, "r") as f:
            return int(f.read())
    return None

def play_game(x, y, user_inputs):
    num_gen = random.randint(x, y)
    guess = 5
    attempts = 0
    win = False
    
    for user_guess in user_inputs:
        if guess <= 0:
            break
            
        attempts += 1
        if user_guess == num_gen:
            win = True
            break
        elif user_guess < num_gen:
            print(f"adde mn bozorgtre dobre emhtn kn: hads baqi mande: {guess-1}\n")
        else:
            print(f"adde mn kochiktre tedad hads baqi mande : {guess-1}\n")
        guess -= 1
    
    return win, attempts, num_gen

def main():
    record_file = "record.txt"
    best_record = load_best_record(record_file)
    
    while True:
        if best_record is not None:
            print(f"Record Qabli: {best_record} hads")
        else:
            print("hanoz revordi sabt nashode")
        
        try:
            x = int(input("Adde aval ra vared konid (Ebtedaye baze)"))
            y = int(input("Adde dovom ra vared konid (Payan baze)"))
        except ValueError:
            print("Lotfan adade sahih vared konid.")
            continue
        
        num_gen = random.randint(x, y)
        guess = 5
        attempts = 0
        win = False

        while guess > 0:
            try:
                user_guess = int(input(f"add ra hads beznid.. hads baqi mande :{guess}\n")) 
            except ValueError:
                print("Lotfan adade sahih vared konid.")
                continue

            attempts += 1
            if user_guess == num_gen:
                print("Afrin Dorost Hads zadi.")
                win = True
                if best_record is None or attempts < best_record:
                    print(f"record jadid to fght ba : {attempts} bar talash sabt shod . Wooooow")
                    with open(record_file, "w") as f:
                        f.write(str(attempts))
                    best_record = attempts
                break
            elif user_guess < num_gen:
                print(f"adde mn bozorgtre dobre emhtn kn: hads baqi mande: {guess-1}\n")
            else:
                print(f"adde mn kochiktre tedad hads baqi mande : {guess-1}\n")
            guess -= 1
            
            if guess == 0:
                print(f"motasfm .tedad hads shoma tamam shod add man : {num_gen} bod . shoma bakhtid\n ")
        
        again = input("mikhay dobare bazi koni (Y/N)\n").strip().lower()
        if again != "y":
            print("Khoshhal shodim ke ba shoma bazi kardim. Khodahafez!")
            break

if __name__ == "__main__":
    main()