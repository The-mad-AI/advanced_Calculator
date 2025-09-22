import time
from functools import wraps


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[LOG] ejraye tabe: {func.__name__} vorodi ha: {args[1:] if len(args) > 1 else ''}")
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start
            print(f"[LOG] tabe {func.__name__} zaman ejra . ba movafghiat ejra shod : {duration:.4f}sanie")
            return result
        except Exception as e:
            with open("error,log", "a", encoding="utf-8") as f :
                f.write(f"khata dar {func.__name__}: {e}\n")
            print(f"[ERROR] khataei rokh dad: {e}")
    return wrapper


class Task:
    def __init__(self, title):
        self.title = title
        self.status = "dar hale anjam"
        
    def mark_done(self):
        self.status = "anjam shode"
    
    def __str__(self):
        return f"{self.title} - {self.status}"
    
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    @log_action
    def add_task(self,title):
        self.tasks.append(Task(title))
    
    @log_action
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise IndexError("shomare vazife na motabar ast")
    @log_action
    def show_tasks(self):
        if not self.tasks:
            print("hich vazife ei sabt nashode ")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")
                
    @log_action
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
        else:
            raise IndentationError("shomare vazife na motabr ast")