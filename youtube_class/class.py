class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"my name is {self.name} , i am {self.age} years old , and i live in {self.city}")

    def have_birthday(self):
        self.age += 1


p1 = Person("Qasem", 27, "Karaj")
p1.introduce()
p1.have_birthday()
p1.introduce()
