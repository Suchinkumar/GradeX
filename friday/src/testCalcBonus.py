import os, sys
import unittest

# import calcBonus
from calcBonus import get_bonus_score 

class testGetBonusScore(unittest.TestCase):
    
    def test_all_zeros(self):
        allTime = [0, 0, 0, 0]
        maxM = 100
        expected = [0, 0, 0, 0]
        self.assertEqual(get_bonus_score(allTime, maxM), expected)
    
    def test_all_max(self):
        allTime = [10, 10, 10, 10]
        maxM = 100
        expected = [100, 100, 100, 100]
        self.assertEqual(get_bonus_score(allTime, maxM), expected)
    
    def test_mixed(self):
        allTime = [5, 6, 8, 10]
        maxM = 100
        expected = [100, 75.0, 50.0, 25.0]
        self.assertEqual(get_bonus_score(allTime, maxM), expected)
               
    
if __name__ == '__main__':
    unittest.main()