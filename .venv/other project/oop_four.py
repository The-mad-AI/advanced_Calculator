class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.ages = age
        self.sound = sound

    def print_info(self):
        print(f"name heyvan {self.name}")
        print(f"gone heyvan {self.species}")
        print(f"sene heyvan {self.ages}")
        print(f"sedaye heyvan {self.sound}")
        
    def make_sound(self):
        print(self.sound)
        
class Zoo_name:
    def __init__(self, name):
        self.name = name
        print(self.name)
            
            
class Bird(Animal):
    def wing_span(self):
        print(f"the wing span is ")
    def make_sound(self):
        pass
        
        
    lion = Animal("lion", "gorbesan", "5 sal", "ghoresh")
    lion.print_info()
    lion.make_sound()