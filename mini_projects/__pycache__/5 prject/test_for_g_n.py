import unittest
import os
from unittest.mock import patch, MagicMock
from g_n import load_best_record, play_game  # your_game_module را با نام فایل خود جایگزین کنید

class TestNumberGuessGame(unittest.TestCase):
    
    def setUp(self):
        # ایجاد یک فایل رکورد موقت برای تست
        with open("test_record.txt", "w") as f:
            f.write("3")
    
    def tearDown(self):
        # پاک کردن فایل رکورد بعد از تست
        if os.path.exists("test_record.txt"):
            os.remove("test_record.txt")
    
    def test_load_best_record_exists(self):
        # تست وجود داشتن رکورد
        result = load_best_record("test_record.txt")
        self.assertEqual(result, 3)
    
    def test_load_best_record_not_exists(self):
        # تست عدم وجود رکورد
        result = load_best_record("non_existent_file.txt")
        self.assertIsNone(result)
    
    @patch('random.randint')
    def test_play_game_win(self, mock_randint):
        # تست بردن در بازی
        mock_randint.return_value = 5
        win, attempts, target = play_game(1, 10, [5])
        
        self.assertTrue(win)
        self.assertEqual(attempts, 1)
        self.assertEqual(target, 5)
    
    @patch('random.randint')
    def test_play_game_lose(self, mock_randint):
        # تست باختن در بازی
        mock_randint.return_value = 5
        win, attempts, target = play_game(1, 10, [1, 2, 3, 4, 6])
        
        self.assertFalse(win)
        self.assertEqual(attempts, 5)
        self.assertEqual(target, 5)
    
    @patch('random.randint')
    def test_play_game_partial_win(self, mock_randint):
        # تست بردن در تلاش های میانی
        mock_randint.return_value = 5
        win, attempts, target = play_game(1, 10, [1, 2, 3, 4, 5, 6, 7])
        
        self.assertTrue(win)
        self.assertEqual(attempts, 5)  # در تلاش پنجم برده
        self.assertEqual(target, 5)

if __name__ == "__main__":
    unittest.main()