import unittest
import Day09.day9 as day

class Day9Tests(unittest.TestCase):
    def test_day_9_part_one(self):
        self.assertEqual(day.part_one(), 88311122)

    def test_day_9_part_two(self):
        self.assertEqual(day.part_two(), 13549369)

if __name__ == '__main__':
    unittest.main()        