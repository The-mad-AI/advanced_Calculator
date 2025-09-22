import math
import os
from typing import Union, Optional


class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    def clear_screen(self):
        """پاک کردن صفحه نمایش / Clear the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def add_to_history(self, operation: str, result: Union[int, float, str]):
        """اضافه کردن عملیات به تاریخچه / Add operation to history"""
        self.history.append(f"{operation} = {result}")

    def add(self, a: float, b: float) -> float:
        """جمع دو عدد / Add two numbers"""
        result = a + b
        self.add_to_history(f"{a} + {b}", result)
        return result

    def subtract(self, a: float, b: float) -> float:
        """تفریق دو عدد / Subtract two numbers"""
        result = a - b
        self.add_to_history(f"{a} - {b}", result)
        return result

    def multiply(self, a: float, b: float) -> float:
        """ضرب دو عدد / Multiply two numbers"""
        result = a * b
        self.add_to_history(f"{a} * {b}", result)
        return result

    def divide(self, a: float, b: float) -> Union[float, str]:
        """تقسیم دو عدد / Divide two numbers"""
        if b == 0:
            return "خطا: تقسیم بر صفر مجاز نیست / Error: Division by zero is not allowed"
        result = a / b
        self.add_to_history(f"{a} / {b}", result)
        return result

    def power(self, base: float, exponent: float) -> float:
        """محاسبه توان / Calculate power"""
        result = math.pow(base, exponent)
        self.add_to_history(f"{base} ^ {exponent}", result)
        return result

    def square_root(self, n: float) -> Union[float, str]:
        """محاسبه جذر / Calculate square root"""
        if n < 0:
            return "خطا: جذر اعداد منفی تعریف نشده است / Error: Square root of negative numbers is undefined"
        result = math.sqrt(n)
        self.add_to_history(f"√{n}", result)
        return result

    def percentage(self, value: float, total: float) -> float:
        """محاسبه درصد / Calculate percentage"""
        result = (value / total) * 100
        self.add_to_history(f"{value}% of {total}", result)
        return result

    def memory_add(self, value: float) -> float:
        """افزودن به حافظه / Add to memory"""
        self.memory += value
        self.add_to_history(f"M+ {value}", self.memory)
        return self.memory

    def memory_subtract(self, value: float) -> float:
        """کاهش از حافظه / Subtract from memory"""
        self.memory -= value
        self.add_to_history(f"M- {value}", self.memory)
        return self.memory

    def memory_recall(self) -> float:
        """خواندن از حافظه / Recall from memory"""
        return self.memory

    def memory_clear(self) -> float:
        """پاک کردن حافظه / Clear memory"""
        self.memory = 0
        self.add_to_history("MC", 0)
        return 0

    def show_history(self):
        """نمایش تاریخچه / Show calculation history"""
        if not self.history:
            print("تاریخچه خالی است / History is empty")
            return
        print("\nتاریخچه محاسبات / Calculation History:")
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")


def get_valid_number(prompt: str) -> Optional[float]:
    """دریافت عدد معتبر از کاربر / Get valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("لطفا یک عدد معتبر وارد کنید / Please enter a valid number")


def main():
    calc = Calculator()

    while True:
        calc.clear_screen()
        print("=== ماشین حساب پیشرفته / Advanced Calculator ===")
        print("1. جمع / Add")
        print("2. تفریق / Subtract")
        print("3. ضرب / Multiply")
        print("4. تقسیم / Divide")
        print("5. توان / Power")
        print("6. جذر / Square Root")
        print("7. درصد / Percentage")
        print("8. حافظه / Memory Operations")
        print("9. تاریخچه / History")
        print("10. خروج / Exit")

        choice = input("\nانتخاب کنید / Select an option: ")

        if choice == "10":
            print("خداحافظ / Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5"]:
            num1 = get_valid_number("عدد اول / First number: ")
            num2 = get_valid_number("عدد دوم / Second number: ")

            if choice == "1":
                result = calc.add(num1, num2)
            elif choice == "2":
                result = calc.subtract(num1, num2)
            elif choice == "3":
                result = calc.multiply(num1, num2)
            elif choice == "4":
                result = calc.divide(num1, num2)
            else:  # choice == "5"
                result = calc.power(num1, num2)

        elif choice == "6":
            num = get_valid_number("عدد را وارد کنید / Enter number: ")
            result = calc.square_root(num)

        elif choice == "7":
            value = get_valid_number("مقدار / Value: ")
            total = get_valid_number("کل / Total: ")
            result = calc.percentage(value, total)

        elif choice == "8":
            print("\nعملیات حافظه / Memory Operations:")
            print("1. افزودن به حافظه / Add to memory")
            print("2. کاهش از حافظه / Subtract from memory")
            print("3. خواندن از حافظه / Recall from memory")
            print("4. پاک کردن حافظه / Clear memory")

            mem_choice = input("انتخاب کنید / Select an option: ")
            if mem_choice == "1":
                num = get_valid_number("عدد را وارد کنید / Enter number: ")
                result = calc.memory_add(num)
            elif mem_choice == "2":
                num = get_valid_number("عدد را وارد کنید / Enter number: ")
                result = calc.memory_subtract(num)
            elif mem_choice == "3":
                result = calc.memory_recall()
            elif mem_choice == "4":
                result = calc.memory_clear()
            else:
                print("گزینه نامعتبر / Invalid option")
                continue

        elif choice == "9":
            calc.show_history()
            input("\nبرای ادامه Enter را فشار دهید / Press Enter to continue...")
            continue

        else:
            print("گزینه نامعتبر / Invalid option")
            continue

        print(f"\nنتیجه / Result: {result}")
        input("\nبرای ادامه Enter را فشار دهید / Press Enter to continue...")


if __name__ == "__main__":
    main()
