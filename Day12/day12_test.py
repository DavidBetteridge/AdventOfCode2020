import unittest
import Day12.day12 as day

class Day12Tests(unittest.TestCase):
    def test_day_12_part_one(self):
        self.assertEqual(day.part_one(), 1010)

    def test_day_12_part_two(self):
        self.assertEqual(day.part_two(), 52742)

if __name__ == '__main__':
    unittest.main()        