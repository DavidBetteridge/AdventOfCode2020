import unittest
import Day01.day1 as day

class Day1Tests(unittest.TestCase):
    def test_day_1_part_one(self):
        self.assertEqual(day.part_one(), 1003971)

    def test_day_2_part_two(self):
        self.assertEqual(day.part_two(), 84035952)

if __name__ == '__main__':
    unittest.main()        