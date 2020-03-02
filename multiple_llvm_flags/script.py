import os
import subprocess
import argparse
import sys
import itertools

def readFile(filename):
    with open(filename, 'r') as f:
        return [line[:-1] for line in f]

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

def run(what, otherflags):
    return subprocess.check_output(what + otherflags)

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
    argparser.add_argument("-l", "--llvm-file", dest="llvms", default=os.path.join('.', 'llvms'), help="LLVM filepath")
    argparser.add_argument("-b", "--build-path", dest="buildfolder", default=os.path.join('.', 'build'), help="LLVM build folder")
    argparser.add_argument("-x", "--expression", dest="regex", default="[a-c]", help="Regular expression")
    argparser.add_argument("-t", "--target", dest="target", default=os.path.join('.', 'script.py'), help="File target for comparison")
    args, otherflags = argparser.parse_known_args()

    flagset = pipe(args.flags, readFile, allCombinations)
    folders = findLLVMFolders(args.llvms)
    for flags in flagset:
        mapFn = lambda folder: pipe(
                    flags,
                    breakFlagsIfNeeded,
                    lambda flgs: mkname(folder, args.regex, args.target, flgs, args.buildfolder),
                    lambda c: run(c, otherflags)
                )
        result = pipe(map(mapFn, folders), lambda arr: map(str, arr))
        print(" ".join(result))
