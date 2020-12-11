import unittest
import Day02.day2 as day

class Day2Tests(unittest.TestCase):
    def test_day_2_part_one(self):
        self.assertEqual(day.part_one(), 460)

    def test_day_2_part_two(self):
        self.assertEqual(day.part_two(), 251)

if __name__ == '__main__':
    unittest.main()        