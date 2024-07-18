import argparse
import os
from extract import extractAndList
from runner import runTest
from grader import addMarks
from calcBonus import get_bonus_score
from cleanup import removeAllExtracted
import concurrent.futures
from createJSON import csv_to_json

if __name__ == "__main__":
    # start = time.time()
    parser = argparse.ArgumentParser(description='Main arg parser')
    parser.add_argument('-i', '--input-path', type=str, dest='zippath',
                        required=True, help='input path for the zip')
    parser.add_argument('-ti', '--test-case-path', type=str, dest='testpath',
                        required=True, help='input path for the zip')
    parser.add_argument('-o', '--output-path', type=str, dest='outpath',
                        default='../testResults.csv', help='output path for the extraction')
    parser.add_argument('-r', '--record-time', action='store_true', dest='checkTime', help='use to record runtime')
    parser.add_argument('-m', '--max-bonus-score', type=int, dest='maxB',
                        default=10, help='maximum bonus score')
    parser.add_argument('-to', '--timeout', type=int, dest='timeOut',
                        default=60, help='set timeout for each testcase')
    #parser.add_argument('-cl', '--clang', action='store_true', dest='useClang', help='use clang instead of gcc')
   #
    parser.add_argument('-lng', '--language', type=str, dest='language', required=True, help='Choose language to test')
    parser.add_argument('-pn', '--problem-num', type=str, dest='pname',
                        default='', help='use to specify a specific problem number')
    parser.add_argument('-ww', '--without-whitespace', action='store_true', dest='raWhitespaces',
                        help='comparison after removing all whitespaces from I/O')
    parser.add_argument('-abs', '--absolute-comparison', action='store_true', dest='kWhitespaces',
                        help='char by char comparison ')

    args = parser.parse_args()

    # if args.useClang:
    #     cname = 'clang'
    # else:
    #     cname = 'gcc'
    # cname = 'g++'

    # Allocate different Compiler Tags and File Extensions according to input type
    match args.language:
        case "C":
            cname = 'gcc'
            fileExtension = '.c'
        case "Clang":
            cname = 'clang'
            fileExtension = '.c'
        case "CPP":
            cname = 'g++'
            fileExtension = '.cpp'
        case "Python":
            cname = 'python3'
            fileExtension = '.py'
        case "Java":
            cname = 'javac'
            fileExtension = '.java'
        case default:
            cname = 'g++'
            fileExtension = '.cpp'

    # print(fileExtension)

    if args.raWhitespaces:
        compType = 'rAll'
    elif args.kWhitespaces:
        compType = 'abs'
    else:
        compType = 'part'

    if not os.path.isfile(args.zippath):
        raise ValueError("File(Zip Input) doesn't exist")
    if not os.path.isfile(args.testpath):
        raise ValueError("File(Test Case) doesn't exist")

    zip_dir = args.zippath

    all_files = extractAndList(zip_dir, args.pname, fileExtension)
    files_dir = ".".join(zip_dir.split('.')[:-1])

    # print(files_dir)

    casesPassed = []
    timetaken = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [
            executor.submit(runTest, args.testpath, files_dir, file, args.timeOut, cname, fileExtension, compType) for
            file in all_files]

        for returnVal in concurrent.futures.as_completed(results):
            casesPassed.append(returnVal.result()[0])
            if args.checkTime:
                timetaken.append(returnVal.result()[1])

    # for file in all_files:
    #     # print("Gets inside loop")
    #     test_result, time = runTest(args.testpath, files_dir, file, args.timeOut, cname, fileExtension, compType)
    #     # print(test_result)
    #     # print(time)
    #     casesPassed.append(test_result)
    #     if args.checkTime:
    #         timetaken.append(time)
    bScore = []

    if args.checkTime:
        bScore = get_bonus_score(timetaken, args.maxB)
    addMarks(all_files, args.outpath, casesPassed, args.testpath, bScore, fileExtension)

    removeAllExtracted(files_dir)
    print(args.outpath)
      
    csv_to_json(args.outpath,args.testpath)
    # end = time.time()
    # print(end-start)
