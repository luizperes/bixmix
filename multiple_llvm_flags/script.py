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

def run(what):
    return subprocess.check_output(what)

def mkname(folder, regex, target, flags, buildfolder):
    buildpath = os.path.join(buildfolder, os.path.join(folder, "bin/icgrep"))
    command = pipe([buildpath, regex, target], lambda lst: lst + flags)
    print(str(command))
    return command

def breakFlagsIfNeed(flags):
    newFlags = []
    for f in flags:
        newFlags.extend(f.split())
    return newFlags

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-c", "--flags-file", dest="flags", default=os.path.join('.', 'flags'), help="flags filepath")
    argparser.add_argument("-b", "--build-path", dest="buildfolder", default=os.path.join('.', 'build'), help="LLVM build folder")
    argparser.add_argument("-e", "--expression", dest="regex", default="[a-c]", help="Regular expression")
    argparser.add_argument("-t", "--target", dest="target", default=os.path.join('.', 'script.py'), help="File target for comparison")
    args = argparser.parse_args()

    flagset = pipe(args.flags, readFile, allCombinations)
    folders = [""]
    for flags in flagset:
        mapFn = lambda folder: pipe(
                    flags,
                    breakFlagsIfNeed,
                    lambda flgs: mkname(folder, args.regex, args.target, flgs, args.buildfolder),
                    lambda c: run(c)
                )
        result = pipe(map(mapFn, folders), list)
        print("".join(result))
