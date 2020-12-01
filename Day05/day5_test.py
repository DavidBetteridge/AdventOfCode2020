import unittest
import Day05.day5 as day

class Day5Tests(unittest.TestCase):
    def test_day_5_part_one(self):
        self.assertEqual(day.part_one(), 813)

    def test_day_5_part_two(self):
        self.assertEqual(day.part_two(), 612)

if __name__ == '__main__':
    unittest.main()        