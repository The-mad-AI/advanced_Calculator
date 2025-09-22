import math
from typing import  Optional
import os

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        
    def clear_screen(self):
        os.system("cls" if os.name == 'nt' else "clear")
        
    def add_to_history(self, operation : str, result : float| str| int):
        self.history.append(f"{operation} = {result}")
        
    def add(self, a:float, b:float) -> float:
        result = a + b
        self.add_to_history(f"{a} + {b}", result)
        return result
    
    def subtract(self, a:float, b:float) -> float:
        result = a - b
        self.add_to_history(f"{a} - {b}", result)
        return result
    
    def multiply(self, a:float, b:float) -> float:
        result = a * b
        self.add_to_history(f"{a} × {b}", result)
        return result
    
    def divide(self, a:float, b:float) -> float | str:
        if b == 0:
            exept_error = "Error: Division by zero is not allowed"
            self.add_to_history(f"{a} ÷ {b}", exept_error)
            return exept_error
        result = a / b
        self.add_to_history(f"{a} ÷ {b}", result)
        return result
    
    def power(self, base:float, exponent:float) -> float:
        result = math.pow(base, exponent)
        self.add_to_history(f"{base} ^ {exponent}", result)
        return result
    
    def square_root(self, n:float) -> float | str:
        if n < 0:
            return "square root of negative numbers is undefined"
        result = math.sqrt(n)
        self.add_to_history(f"{n} √ ", result)
        return result
    
    def percentage(self, value:float, total:float) -> float:
        result = (value / total) * 100
        self.add_to_history(f"{value} % of {total}", result)
        return result
    
    def memory_add(self, value:float) -> float:
        self.memory += value
        self.add_to_history(f"+M {value}", self.memory)
        return self.memory
    
    def memory_subtract(self, value:float) -> float:
        self.memory -= value
        self.add_to_history(f"-M {value}", self.memory)
        return self.memory
    
    def memory_recall(self) -> float:
        return self.memory
    
    def memory_clear(self) -> float:
        self.memory = 0
        self.add_to_history("MC", 0)
        return 0
    
    def show_history(self):
        if not self.history:
            print("history is empty")
            return
        print("calculation history:")
        for i , calc in enumerate(self.history, 1):
            print(f"{i}, {calc}")
        
def get_valid_number(prompt:str)-> Optional[float]:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("enter a valid number")
            
def main():
    calc = Calculator()
    
    while True:
        calc.clear_screen()
        print("______Advanced caculator_____")
        print("1-add")
        print("2-subtract")
        print("3-multiply")
        print("4-divide")
        print("5-power")
        print("6-square root")
        print("7-percentage")
        print("8-memory operations")
        print("9-history")
        print("10-Exit")
        
        
        choice = input("select an option: \n")
        
        if choice == "10":
            print("Good Bye")
            break
            
        if choice in ['1', '2', '3', '4', '5'] :
            num1 = get_valid_number("first num : ")
            num2 = get_valid_number("second number: ")
            
            if choice == '1':
                result = calc.add(num1, num2)
            elif choice == '2':
                result = calc.subtract(num1, num2)
            elif choice == '3':
                result = calc.multiply(num1, num2)
            elif choice == '4':
                result = calc.divide(num1, num2)
            else :
                result = calc.power(num1 , num2)
            
        elif choice == '6':
            num = get_valid_number("Enter a valid number: ")
            result = calc.square_root(num)
            
        elif choice == '7':
            value = get_valid_number("value = ")
            total = get_valid_number("Total = ")
            result = calc.percentage(value, total)
            
        elif choice == '8':
            print("memory operation")
            print("1-memory add")
            print("2-memory subtract")
            print("3-memory recall")
            print("4-memory clear")
            
            mm_choice = input("select an option: ")
            if mm_choice == '1':
                num = get_valid_number("Enter number : ")
                result = calc.memory_add(num)
            elif mm_choice == '2':
                num = get_valid_number("enter number")
                result = calc.memory_subtract(num)
            elif mm_choice == '3':
                result = calc.memory_recall()
            elif mm_choice == '4':
                result = calc.memory_clear()
                print("Memory is Cleared")
            else :
                print("Error : Invalid Option")
                continue
            
        elif choice == '9':
            result = calc.show_history()
            input("Press Enter to continue")
            continue
        
        else :
            print("Error : Invalid Option")
            continue
        
        print(f"result : {result}")
        input("Press Enter to continue......")
        
        
if __name__ == "__main__":
    main()