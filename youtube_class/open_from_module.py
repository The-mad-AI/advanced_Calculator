with open("message.txt", "w") as file:
    file.write("Hello world")

with open("message.txt", "r") as file:
    content = file.read()
    print(content)
with open("message.txt", "r") as file:
    for line in file:
        print(line.strip())


import os
filename = "empty.txt"

if os.path.exists(filename) and os.path.getsize(filename) == 0:
    print("file is empty")
else:
    print("file not empty")

with open("notes.txt", "a") as file:
    file.write("\n this is a new line ")
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(f"تعداد خطوط : {len(lines)}")


with open("notes.txt", "r") as file:
    counter = 1
    for file in line:
        print(f"{counter} ==> {line}")
        counter += 1
