import os, sys
import unittest
import json

from runner import runTest

class TestRunTest(unittest.TestCase):
    def test_runTest_compilation_success(self):
        # Test compilation success
        testCasePath = "../test/TestZips/testCases.json"
        filesPath = "../test/TestZips"
        filename = "test.c"
        timeOut = 1
        cname = "gcc"
        fileExtension = ".c"
        compType = "text"
        expected_output = [0, 0]
        actual_output, exec_time = runTest(testCasePath, filesPath, filename, timeOut, cname, fileExtension, compType)
        self.assertEqual(expected_output, actual_output)
        self.assertGreater(exec_time, -0.5)

    def test_runTest_compilation_failure(self):
        # Test compilation failure
        testCasePath = "../test/TestZips/testCases.json"
        filesPath = "../test/TestZips"
        filename = "test_err.c"
        timeOut = 1
        cname = "gcc"
        fileExtension = ".c"
        compType = "text"
        expected_output = [0, 0]
        actual_output, exec_time = runTest(testCasePath, filesPath, filename, timeOut, cname, fileExtension, compType)
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(exec_time, 0)

    def test_runTest_execution_success(self):
        # Test execution success
        testCasePath = "../test/TestZips/testCases.json"
        filesPath = "../test/TestZips"
        filename = "test.py"
        timeOut = 1
        cname = "python3"
        fileExtension = ".py"
        compType = "text"
        expected_output = [0,0]
        actual_output, exec_time = runTest(testCasePath, filesPath, filename, timeOut, cname, fileExtension, compType)
        self.assertEqual(expected_output, actual_output)
        self.assertGreater(exec_time, 0)

    def test_runTest_execution_timeout(self):
        # Test execution timeout
        testCasePath = "../test/TestZips/testCases.json"
        filesPath = "../test/TestZips"
        filename = "test_timeout.py"
        timeOut = 1
        cname = "python3"
        fileExtension = ".py"
        compType = "text"
        expected_output = [0, 0]
        actual_output, exec_time = runTest(testCasePath, filesPath, filename, timeOut, cname, fileExtension, compType)
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
