import unittest
import Day10.day10 as day

class Day10Tests(unittest.TestCase):
    def test_day_10_part_one(self):
        self.assertEqual(day.part_one(), 2240)

    def test_day_10_part_two(self):
        self.assertEqual(day.part_two(), 49607173328384)

if __name__ == '__main__':
    unittest.main()        