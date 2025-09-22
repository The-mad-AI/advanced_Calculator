import json

class contacts_manager:
    def __init__(self):
        self.contacts_list = []
    
    def add_contact(self, name, number):
        new_contact  = {'name' : name, 'number' : number}
        if new_contact in self.contacts_list:
            print("the contact is already saved")
            return False
        else:
            self.contacts_list.append({
            'name': name ,
            'number' : number , 
        
        })

    
    def search(self, name):
        for cont in self.contacts_list:
            if name.lower() in cont['name'].lower():
                print(cont)
            else:
                print("contact is not exist")
    
    def backup(self):
        with open("./back_contact.json", "w") as f :
            json.dump(self.contacts_list, f )
    
    def print(self):
        print(self.contacts_list)
    
    
c = contacts_manager()
c.add_contact('QASEM', 7221)
c.add_contact('QASEM', 7221)

c.print()