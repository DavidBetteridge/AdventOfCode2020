import unittest
import Day03.day3 as day

class Day3Tests(unittest.TestCase):
    def test_day_3_part_one(self):
        self.assertEqual(day.part_one(), 254)

    def test_day_3_part_two(self):
        self.assertEqual(day.part_two(), 1666768320)

if __name__ == '__main__':
    unittest.main()        