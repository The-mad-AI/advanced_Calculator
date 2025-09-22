class Car:
    def __init__(self,brand):
        self.brand = brand
        
    def Drive(self):
        print(f"Driving a {self.brand}")
        
        
c = Car("GTR")
c.Drive()




class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"hello {self.name}")

n = Person("Qasem")
n.say_hello()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_information_of_book(self):
        print(f"{self.title} written by {self.author}")
        
b = Book("bi navayan","viktor hogo")
b.show_information_of_book()


class Student(Person):
    def study(self):
        print(f"{self.study} is studying Python OOP")
        
        
        
        
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def masahat(self):
        return self.width * self.height

m = Rectangle(6, 4)
print(m.masahat())



class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else :
            print("Insufficient funds")
    
    
class Animal:
    def __init__(self):
        pass
    def speak(self):
        pass
    
    
class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    def speak(self):
        print("Meow")

