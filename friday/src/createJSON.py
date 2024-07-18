import csv
import json

def getTotalMarks(testCasePath):
    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)
    totalMarks = 0
    for inData in data["test_cases"]:
        totalMarks += inData["marks"]
    return totalMarks

def getTestCases(testCasePath):
    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)
    return len(data["test_cases"])

def getUID(testCasePath):
    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)
        if "uid" in data:
            return data["uid"]
        else:
            return None

def csv_to_json(csv_file_path, testCasePath):
    # Create an empty list to store the student data
    students = []

    # getUID(testCasePath)
    # Open the CSV file and read the data into a dictionary
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Loop through each row of the CSV file and extract the data
        for row in csv_reader:
            rollnumber = row["rollnumber"]
            testcases_passed = row["testcasesPassed"]
            test_score = row["testScore"]

            # Calculate the total marks for the student
            total_marks_student = int(test_score);

            # Create a dictionary to store the student data
            student_data = {
                'rollnumber': rollnumber,
                'testcasesPassed': testcases_passed,
                'totalMarks': str(total_marks_student)
            }

            # Append the student data to the students list
            students.append(student_data)

    # Create a dictionary to store the final JSON data
    json_data = {
        'uid': str(getUID(testCasePath)),
        'totalMarks': str(getTotalMarks(testCasePath)),
        'totalTestCases': str(getTestCases(testCasePath)),
        'students': students
    }

    # Write the JSON data to a file
    with open(csv_file_path[:-3]+'json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)