import unittest
import Day11.day11 as day

class Day11Tests(unittest.TestCase):
    def test_day_11_part_one(self):
        self.assertEqual(day.part_one(), 2329)

    def test_day_11_part_two(self):
        self.assertEqual(day.part_two(), 2138)

if __name__ == '__main__':
    unittest.main()        