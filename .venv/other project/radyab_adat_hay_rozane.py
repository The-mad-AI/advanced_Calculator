from datetime import date

habit_input = input("adat hat ro ba fasele vared kon :")
habits = habit_input.split()

unit_input = input("vahed har adat ro vared kon ")
units = unit_input.split()

value_input = input("tedad ya meghdar  har adat ro vared kon ")
values =list(map(int, value_input.split()))

habit_tracker= {}
for habit, unit, value in zip(habits, units, values):
    habit_tracker[habit] = {"unit": unit, "value": value}
    
    
    
summary =(date.today(), habit_tracker)

def show_summary(*args, **kwargs):
    print("tarikh:", args[0])
    print("kholase rooz:")
    for habit, data in kwargs.items():
        print(f"{habit}: {data['value']} {data['unit']} ")
        
show_summary(summary[0], **summary[1])