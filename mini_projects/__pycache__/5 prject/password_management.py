from cryptography.fernet import Fernet


def save_key():
    with open("./key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    with open("./key.key", "rb") as key_file:
        return key_file.read
    
key = load_key()
fer = Fernet(key)

def add(username, password):
    encry_pass =fer.encrypt(password.encode()).decode()
    with open("./passwordlist", "a") as f:
        f.write(f"{username} - {encry_pass}\n")
        print("added")


def viwe():
    with open("./passwordlist", "r") as f:
        for item in f:
            item = item.strip().split(" - ")
            username, encry_pass = item
            password = fer.decrypt(encry_pass.encode()).decode()
            print(f"Username : {username} Password : {password}")





while True:
    user_select = input("select the mode..... a= add  v=viwe  q=quit\n").lower()
    
    if user_select == "a":
        print("lets add a new username and password")
        username = input("enter the username\n")
        password = input("enter the password\n")
        
        add(username, password)
    
    elif user_select == "v":
        print("this are username and passwords")
        viwe()
        
        
    elif user_select == "q":
        print("bye")
        break