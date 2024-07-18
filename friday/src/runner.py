import atexit
import os
import subprocess
import json
import time
# import atexit
from compiler import compileFile


def changeFormatting(str, compType):
    if compType == 'abs':
        return str
    elif compType == 'part':
        return str.strip()
    elif compType == 'rAll':
        return "".join(str.split())


def runTest(testCasePath, filesPath, filename, timeOut, cname, fileExtension, compType):
    # print("Reaches Test Runner")
    # global process
    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)
    testResult = []

    fullFilePath = os.path.join(filesPath, filename)
    # fullExecPath = os.path.join(filesPath, 'a.out')

    # print(fullFilePath)
    # print(fullExecPath)
    fullExecPath = None
    if cname == 'gcc' or cname == 'g++' or cname == 'clang' or cname == 'javac':
        fullExecPath, compileCheck = compileFile(fullFilePath, filesPath, cname, fileExtension)
        # print(compileCheck)
        if not compileCheck:
            for cases in data["test_cases"]:
                testResult.append(0)
            return testResult, 0

    # print(fullExecPath)
    # p1 = subprocess.Popen([cname, fullFilePath, '-o', fullExecPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                       encoding='utf8')
    # if p1.communicate()[1].find('error:') != -1:
    #     for cases in data["test_cases"]:
    #         testResult.append(0)
    #     return testResult, 0
    # p1.communicate()
    start = time.time()

    # print(start)
    # checkTimout = 1
    for indata in data["test_cases"]:
        if cname == 'gcc' or cname == 'g++' or cname == 'clang':
            # print(fullExecPath)
            process = subprocess.Popen([fullExecPath], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, encoding='utf8')
        elif cname == 'python3':
            # print(fullFilePath)
            process = subprocess.Popen([cname, fullFilePath], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, encoding='utf8')
        elif cname == 'javac':

            # TODO(Hydragyr):
            #   Add user input for memory requirements per file for best execution time

            # NOTE:
            #   2 M Looks like the sweet spot for memory requirements for JVMs
            #   1536k leads to shorter time than 2m
            process = subprocess.Popen([cname[:len(cname) - 1],'-Xmx1536k' ,fullFilePath], stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8')

        process.stdin.write(indata.get("test_case", ""))
        try:
            stdout, stderr = process.communicate(timeout=timeOut)
            if stderr:
                testResult.append(0)
            else:
                if changeFormatting(stdout, compType) == changeFormatting(indata["output"], compType):
                    testResult.append(1)
                else:
                    testResult.append(0)
        except subprocess.TimeoutExpired:
            print("Here2")
            process.kill()
            testResult.append(0)

    end = time.time()

    # TODO(Hydragyr):
    #   Add process killing for 'process'.

    # process.kill()
    # atexit.register(process.kill)
    return testResult, (end - start)  # * checkTimout
