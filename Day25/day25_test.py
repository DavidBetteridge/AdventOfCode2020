import unittest
import Day25.day25 as day

class Day1Tests(unittest.TestCase):
    def test_day_25_part_one(self):
        self.assertEqual(day.part_one(), 8740494)

if __name__ == '__main__':
    unittest.main()        