import csv
import json


def get_stu_name(filename,fileExtension):
    extensionLen= len(fileExtension)
    return filename.split('_')[-1][:-1*extensionLen]


def addMarks(fileNames, outPath, testPassList, testCasePath, bScore,fileExtension):
    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)

    allMarks = []
    allCasesPassed = []
    j = 0
    for student in testPassList:
        i = 0
        totalMarks = 0
        casesPassed = 0
        for inData in data["test_cases"]:
            casesPassed += testPassList[j][i]
            totalMarks = totalMarks + (testPassList[j][i] * inData["marks"])
            i += 1
        allCasesPassed.append(casesPassed)
        allMarks.append(totalMarks)
        j += 1

    with open(outPath, 'w') as file:
        writer = csv.writer(file)

        if bScore:
            writer.writerow(["rollnumber", "testScore","testcasesPassed", "TimeScore"])
            for k in range(len(fileNames)):
                writer.writerow([get_stu_name(fileNames[k],fileExtension), allMarks[k], allCasesPassed[k], bScore[k]])
        else:
            writer.writerow(["rollnumber", "testScore","testcasesPassed"])
            for k in range(len(fileNames)):
                # print(get_stu_name(fileNames[k],fileExtension))
                writer.writerow([get_stu_name(fileNames[k],fileExtension), allMarks[k], allCasesPassed[k]])
    return 0
