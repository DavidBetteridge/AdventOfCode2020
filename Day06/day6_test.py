import unittest
import Day06.day6 as day

class Day6Tests(unittest.TestCase):
    def test_day_6_part_one(self):
        self.assertEqual(day.part_one(), 6585)

    def test_day_6_part_two(self):
        self.assertEqual(day.part_two(), 3276)

if __name__ == '__main__':
    unittest.main()        