l = [ 1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20]
def just_even(n):
    count = 0
    sum_even = []
    for nums in n:
        if nums %2 == 0:
            count += nums
            sum_even.append(nums)
    return count, sum_even

total_even , show_even = just_even(l)

print("majome adad zoj :", total_even)
print("list adad zoj:", show_even)



def tavan_se(n):
    return list(map(lambda x : x**3 , n))

    
print(tavan_se(l))


my_list = ['apple', 'banana', 'kiwi', 'mango']

more_than_5 = list(filter(lambda x : len(x) > 5 , my_list))

for f in more_than_5:
    print(f)
    
    


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return self.name , self.age
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def print_student_id(self):
        return self.student_id
    

c =Person("Qasem", 28)
d = Student("Qasem", 28, 149875)
print(d.age, d.name , d.student_id)






numbers = []
for i in range(5):
    nums =float(input(f"add {i+1} ra vared konid "))
    numbers.append(nums)
    
doubeld_numbers = list(map(lambda x : x*2 , numbers))
print(doubeld_numbers, "adad do brabar shode")

total = 0
for nums in doubeld_numbers:
    total += nums
print(total, "majom adad jadid")
    
class Calculator:
    def average(self, num_list):
        if len(num_list) == 0:
            return 0
        return sum(num_list) / len(num_list)
    
calc = Calculator()
avg = calc.average(doubeld_numbers)
print(avg, 'miangin adad jadid')