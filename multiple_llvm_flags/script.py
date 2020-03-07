#!/usr/bin/env python3

import os
import subprocess
import argparse
import sys
import itertools
from datetime import datetime

def readFile(filename):
    with open(filename, 'r') as f:
        return [line[:-1] for line in f]

def saveInFile(filename, what):
    with open(filename, 'a') as f:
        f.write(what + "\n")

def createCSV(filename, delimiter=', '):
    if not os.path.exists(filename):
        value  = "datetime, filename, regular expression, LLVM version, Unicode version, parabix revision, "
        value += "none icgrep compile time, none total time, none asm size, "
        value += "less icgrep compile time, less total time, less asm size, "
        value += "standard icgrep compile time, standard total time, standard asm size, "
        value += "aggressive icgrep compile time, aggressive total time, aggressive asm size"
        with open(filename, 'a') as f:
            f.write(value + "\n")

def allCombinations(args=[]):
    arr = []
    for i in range(len(args)):
        comb = itertools.combinations(args, i + 1)
        for c in comb:
            arr.append(list(c))
    return arr

# apply functions in a pipe, e.g.: 3 |> str |> print would print "3"
def pipe(data, *funcs):
    for func in funcs:
        data = func(data)
    return data

def stripString(s, begin, end, startFrom=None):
    decoded = str(s)
    beginIdx = 0
    if startFrom is not None:
        beginIdx = decoded.find(startFrom)
    posB = decoded.find(begin, beginIdx) + len(begin)
    posE = decoded.find(end, posB)
    return decoded[posB:posE]

def stripVersions(s):
    llvmVersion = stripString(s, "LLVM version ", "\\n")
    unicodeVersion = stripString(s, "Unicode version ", "\\n")
    parabixRevision = stripString(s, "Parabix revision ", "\\n")
    return [llvmVersion, unicodeVersion, parabixRevision]

def stripIcGrepCompileTime(s):
    out = stripString(s, "Execution Time: ", " seconds", "Kernel Generation\\n")
    return [out.strip()]

def stripPerfStatTime(s, padding="per insn"):
    spaces = " " * len(padding)
    out = stripString(s, "\\n\\n", " seconds", "of all branches" + spaces)
    return [out.strip()]

def runAndReturnSizeFile(s, filename):
    out = str(os.path.getsize(filename))
    return [out]

# Append to the CSV file in the format
#
# datetime, filename, regular expression, LLVM version, Unicode version, parabix revision,
# none icgrep compile time, none total time, none asm size,
# less icgrep compile time, less total time, less asm size,
# standard icgrep compile time, standard total time, standard asm size,
# aggressive icgrep compile time, aggressive total time, aggressive asm size
def run(what, otherflags, filename, regex, delimiter=", ", timeout=60, asmFile="asm"):
    output = [str(datetime.now()), filename, regex]
    output += stripVersions(subprocess.check_output(what + ["--version"]))
    command = what + otherflags + ["-enable-object-cache=0"]
    opt_levels = ["none", "less", "standard", "aggressive"]
    for opt_level in opt_levels:
        try:
            command_opt_level = command + ["-backend-optimization-level=" + opt_level]
            output += stripIcGrepCompileTime(subprocess.check_output(command_opt_level + ["-kernel-time-passes"], stderr=subprocess.STDOUT, timeout=timeout))
            output += stripPerfStatTime(subprocess.check_output(["perf", "stat"] + command_opt_level, stderr=subprocess.STDOUT, timeout=timeout))
            output += runAndReturnSizeFile(subprocess.check_output(command_opt_level + ["-ShowASM=" + asmFile], stderr=subprocess.STDOUT, timeout=timeout), asmFile)
        except:
           output += ["inf", "inf", "inf"]
           continue
    return delimiter.join(output)

def mkname(folder, regex, target, flags, buildfolder):
    buildpath = os.path.join(buildfolder, os.path.join(folder, "bin/icgrep"))
    command = pipe([buildpath, regex, target], lambda lst: lst + flags)
    print(str(command))
    return command

def breakFlagsIfNeeded(flags):
    newFlags = []
    for f in flags:
        newFlags.extend(f.split())
    return newFlags

def findLLVMFolders(llvmsfile):
    if not os.path.exists(llvmsfile):
        return [""]
    else:
        return pipe(llvmsfile, readFile)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-c", "--flags-file", dest="flags", default=os.path.join('.', 'flags'), help="flags filepath")
    argparser.add_argument("-f", "--final-file", dest="finalfile", default=os.path.join('.', 'output.csv'), help="output filepath")
    argparser.add_argument("-l", "--llvm-file", dest="llvms", default=os.path.join('.', 'llvms'), help="LLVM filepath")
    argparser.add_argument("-b", "--build-path", dest="buildfolder", default=os.path.join('.', 'build'), help="LLVM build folder")
    argparser.add_argument("-x", "--expression", dest="regex", default="[a-c]", help="Regular expression")
    argparser.add_argument("-t", "--target", dest="target", default=os.path.join('.', 'script.py'), help="File target for comparison")
    args, otherflags = argparser.parse_known_args()

    createCSV(args.finalfile)
    flagset = pipe(args.flags, readFile, allCombinations)
    folders = findLLVMFolders(args.llvms)
    for flags in flagset:
        mapFn = lambda folder: pipe(
                    flags,
                    breakFlagsIfNeeded,
                    lambda flgs: mkname(folder, args.regex, args.target, flgs, args.buildfolder),
                    lambda c: run(c, otherflags, args.target, args.regex)
                )
        result = pipe(map(mapFn, folders), lambda arr: map(str, arr))
        saveInFile(args.finalfile, " ".join(result))
