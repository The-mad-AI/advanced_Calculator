import unittest
from menu import MenuItem
from cafe import Order, Cafe

class TestCafe(unittest.TestCase):
    def test_add_menu_item(self):
        cafe = Cafe()
        cafe.add_menu_item("Coffee", 30000)
        self.assertEqual(len(cafe.menu), 1)
        self.assertEqual(cafe.menu[0].name, "Coffee")
    
    def test_order_total_and_discount(self):
        order = Order()
        item1 = MenuItem("Tea", 20000)
        item2 = MenuItem("Cake", 40000)
        order.add_item(item1)
        order.add_item(item2)
        order.apply_discount(10)
        self.assertAlmostEqual(order.total,54000)
        self.assertAlmostEqual(order.discount, 6000)
        
    def test_save_order_to_file(self):
        order = Order()
        order.add_item(MenuItem("Coffee", 30000))
        order.apply_discount(0)
        order.save_to_file("test_order.json")
        
        with open("test_order.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data[-1]["items"], ["Coffee"])
        self.assertEqual(data[-1]["total"], 30000)

if __name__ == "__main__":
    unittest.main()
