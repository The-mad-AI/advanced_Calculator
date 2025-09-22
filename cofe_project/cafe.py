#مدیریت منو سفارش ها تخفیف ذخیره سازی

from tomlkit import item
from menu import MenuItem
import json

class Order :
    def __init__(self):
        self.items = []
        self.total = 0
        self.discout = 0
    
    def add_item(self, item: MenuItem):
        self.items.append(item)
        self.total += item.price
    
    def apply_discount(self, percent):
        self.discount = self.total * (percent/100)
        self.total -= self.discount

    def save_to_file(self, filename="order.json"):
        data = {
            "items": [item.name for item in self.items],
            "total": self.total,
            "discount": self.discount
        }
        with open(filename, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_from_file(self,filename="orders.json"):
        with open(filename, "r") as f:
            data = json.load(f)
        self.items = [item(name) for name in data["items"]]
        self.total = data["total"]
        self.discount = data["discount"]

class Cafe:
    def __init__(self):
        self.menu = []
    def add_menu_item(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)
        
    def show_menu(self):
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item}")
    
    def load_menu_from_file(filename+"menu.json"):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [MenuItem(d["name"], d["price"]) for d in data]


if __name__ == "__main__":
    cafe = Cafe()
    cafe.add_menu_item("Coffee", 30000)
    cafe.add_menu_item("Tea", 20000)
    cafe.show_menu()

    order = Order()
    order.add_item(cafe.menu[0])
    order.add_item(cafe.menu[1])
    order.apply_discount(10)
    order.save_to_file()
    print("your order has been saved.")