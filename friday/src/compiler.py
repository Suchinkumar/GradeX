import os
import subprocess
import atexit


def compileFile(filePath, folderPath, cname, fileExtension):
    fullExecPath = None

    if cname == 'gcc' or cname == 'g++' or cname == 'clang':
        fullExecPath = filePath[:len(filePath) - len(fileExtension)] + '.out'

        p1 = subprocess.Popen([cname, '-O0', '-g0', filePath, '-o', fullExecPath], stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              encoding='utf8')

    elif cname == 'javac':
        fullExecPath = filePath
        p1 = subprocess.Popen([cname, fullExecPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8')

    if p1.communicate()[1].find('error:') != -1:
        atexit.register(p1.kill)
        return -1, False

    # TODO(Hydragyr):
    #   Add process killing for 'p1'

    # p1.kill()
    # atexit.register(p1.kill())
    return fullExecPath, True
