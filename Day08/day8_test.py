import unittest
import Day08.day8 as day

class Day8Tests(unittest.TestCase):
    def test_day_8_part_one(self):
        self.assertEqual(day.part_one(), 1810)

    def test_day_8_part_two(self):
        self.assertEqual(day.part_two(), 969)

if __name__ == '__main__':
    unittest.main()        