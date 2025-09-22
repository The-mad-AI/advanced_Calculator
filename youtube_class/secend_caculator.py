import math


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def mul(a, b):
    return a*b


def devide(a, b):
    return "Division by zero is not allowed" if b == 0 else a/b


def root(n):
    return "he square root of negative numbers is undefined" if n < 0 else math.sqrt(n)


while True:
    print("calculator")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5.root")
    print("6.Exit")
    choice = input("select an option\n")
    if choice == "6":
        print("goodbye")
        break
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("first number\n"))
        num2 = float(input("secend number\n"))
        if choice == "1":
            print("result:", add(num1, num2))
        elif choice == "2":
            print("result:", subtract(num1, num2))
        elif choice == "3":
            print("result", mul(num1, num2))
        elif choice == "4":
            print("result", devide(num1, num2))
    elif choice == "5":
        num = float(input("enetr your number\n"))
        print("result:", root(num))
    else:
        print("invlid syntax")
