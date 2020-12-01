import unittest
import Day07.day7 as day

class Day7Tests(unittest.TestCase):
    def test_day_7_part_one(self):
        self.assertEqual(day.part_one(), 254)

    def test_day_7_part_two(self):
        self.assertEqual(day.part_two(), 6006)

if __name__ == '__main__':
    unittest.main()        