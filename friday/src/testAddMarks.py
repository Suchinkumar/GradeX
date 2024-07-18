import os, sys
import unittest
import json

from grader import addMarks

class testAddMarks(unittest.TestCase):
        
    def setUp(self):
            # create a temporary test file with some test cases
            self.test_case_data = {"test_cases": [{"marks": 2}, {"marks": 3}, {"marks": 4}]}
            with open("test_cases.json", "w") as f:
                json.dump(self.test_case_data, f)
            
            # create some mock data for testing
            self.fileNames = ["test1.txt", "test2.txt"]
            self.outPath = "out.csv"
            self.testPassList = [[1, 0, 1], [0, 1, 1]]
            self.testCasePath = "test_cases.json"
            self.bScore = [1, 0.5]
            self.fileExtension = ".txt"

    def test_addMarks_returns_zero_on_valid_inputs(self):
        result = addMarks(self.fileNames, self.outPath, self.testPassList, self.testCasePath, self.bScore, self.fileExtension)
        self.assertEqual(result, 0)

    def test_addMarks_creates_correct_output_file(self):
        addMarks(self.fileNames, self.outPath, self.testPassList, self.testCasePath, self.bScore, self.fileExtension)
        self.assertTrue(os.path.isfile(self.outPath))

    def test_addMarks_creates_output_file_with_correct_data(self):
        addMarks(self.fileNames, self.outPath, self.testPassList, self.testCasePath, self.bScore, self.fileExtension)
        with open(self.outPath, 'r') as f:
            data = [line.split(',') for line in f.read().split('\n')]
        expected_data = [
            ['rollnumber', 'testScore', 'testcasesPassed', 'TimeScore'],
            ['test1', '6', '2', '1'],
            ['test2', '7', '2', '0.5'],
            ['']
        ]
        self.assertEqual(data, expected_data)

    def tearDown(self):
        if os.path.isfile(self.outPath):
            os.remove(self.outPath)

if __name__ == '__main__':
    unittest.main()