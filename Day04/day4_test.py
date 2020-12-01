import unittest
import Day04.day4 as day

class Day4Tests(unittest.TestCase):
    def test_day_4_part_one(self):
        self.assertEqual(day.part_one(), 250)

    def test_day_4_part_two(self):
        self.assertEqual(day.part_two(), 158)

if __name__ == '__main__':
    unittest.main()        