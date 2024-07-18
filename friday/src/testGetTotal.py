import os, sys
import unittest
import json


from createJSON import getTotalMarks

class TestGetTotalMarks(unittest.TestCase):
    
    def test_valid_file1(self):
        # Ensure that the function returns the correct total marks for a valid JSON file
        testCasePath = '../test/test_case1.json'
        self.assertEqual(getTotalMarks(testCasePath), 30)
    
    def test_valid_file2(self):
        # Ensure that the function returns the correct total marks for a valid JSON file
        testCasePath = '../test/test_case2.json'
        self.assertEqual(getTotalMarks(testCasePath), 0)
        
    def test_file_not_found(self):
        # Ensure that the function raises a FileNotFoundError for a non-existent JSON file
        testCasePath = 'nonexistent.json'
        with self.assertRaises(FileNotFoundError):
            getTotalMarks(testCasePath)
    
   

    
if __name__ == '__main__':
    unittest.main()