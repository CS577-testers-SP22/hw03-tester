from subprocess import Popen, PIPE
from random import random, seed
from tqdm import tqdm
from pprint import pprint
import json

MAX_TESTS = 100
MAX_INSTANCES = 20
MAX_JOBS = 100
MAX_TIME = 1000
SEED = 1234

seed(SEED)

def generateInput(multiplier=1):
    '''returns a string that is valid input'''
    instances = int(random() * (MAX_INSTANCES)) + 1
    test = f'{instances}'

    for _ in range(instances):
        jobSize = int(random() * (MAX_JOBS * multiplier)) + 1
        test += f'\n{jobSize}'
        for _ in range(jobSize):
            start = int(random() * (MAX_TIME * multiplier)) + 1
            test += f'\n{start} {int(random() * ((MAX_TIME * multiplier) - start)) + start + 1}'

    return test + '\n'

def shell(cmd, stdin=None):
    out, err = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE).communicate(input=stdin.encode())
    return out.decode('utf8'), err.decode('utf8')

getPython = lambda testCase: shell('python3 scheduling.py', stdin=testCase)
getJava = lambda testCase: shell('java Scheduling', stdin=testCase)

tests = dict()

# manual tests
tests['canvas-test-0'] = {'input':"2\n1\n1 4\n3\n1 2\n3 4\n2 6\n", 'output':"1\n2\n"}

tests = {**tests, **{"small-test-0": {
            "input": "3\n5\n1 19\n19 20\n14 15\n16 17\n1 16\n4\n13 18\n3 7\n3 4\n10 20\n1\n11 16\n",
            "output": "3\n2\n1\n"
        },
        "small-test-1": {
            "input": "2\n1\n12 15\n6\n13 17\n8 11\n19 20\n11 12\n11 12\n3 12\n",
            "output": "1\n4\n"
        },
        "small-test-2": {
            "input": "2\n1\n12 14\n6\n3 19\n16 20\n3 9\n1 7\n17 18\n4 20\n",
            "output": "1\n2\n"
        },
        "small-test-3": {
            "input": "1\n9\n1 9\n7 12\n17 19\n16 18\n17 20\n9 18\n17 18\n3 7\n9 11\n",
            "output": "3\n"
        },
        "small-test-4": {
            "input": "2\n9\n10 19\n14 18\n7 17\n17 18\n19 20\n4 18\n15 19\n9 10\n8 9\n3\n1 11\n2 19\n14 16\n",
            "output": "4\n2\n"
        },
        "small-test-5": {
            "input": "3\n1\n6 8\n5\n5 11\n15 20\n11 19\n8 19\n11 18\n2\n12 15\n17 19\n",
            "output": "1\n2\n2\n"
        },
        "small-test-6": {
            "input": "2\n8\n11 15\n3 14\n19 20\n2 8\n1 14\n13 19\n3 7\n9 18\n3\n17 19\n18 20\n11 20\n",
            "output": "3\n1\n"
        },
        "small-test-7": {
            "input": "2\n7\n17 20\n2 7\n9 19\n6 8\n8 11\n15 18\n2 18\n5\n16 17\n7 8\n8 14\n14 17\n9 15\n",
            "output": "3\n3\n"
        },
        "small-test-8": {
            "input": "1\n4\n13 15\n11 20\n10 17\n14 19\n",
            "output": "1\n"
        },
        "small-test-9": {
            "input": "3\n7\n3 10\n16 17\n3 19\n12 20\n16 20\n6 16\n7 20\n3\n4 18\n6 14\n13 16\n4\n7 11\n16 19\n11 19\n6 8\n",
            "output": "2\n1\n2\n"
        }
    }
}

# random tests
for i in tqdm(range(MAX_TESTS)):
    test = generateInput()
    # print(test)
    java, jerr = getJava(test)
    python, perr = getPython(test)
    if java != python:
        print(f'Java\n{java}')
        print()
        print(f'Java error\n{jerr}')
        print()
        print(f'Python\n{python}')
        print()
        print(f'Python error\n{jerr}')
        print()
        print(f'Input\n{test}')
        exit()
    tests[f'medium-test-{i}'] = {'input':test, 'output':python}

for i in tqdm(range(5)):
    test = generateInput(multiplier=10)
    # print(test)
    java, jerr = getJava(test)
    python, perr = getPython(test)
    if java != python:
        print(f'Java\n{java}')
        print()
        print(f'Java error\n{jerr}')
        print()
        print(f'Python\n{python}')
        print()
        print(f'Python error\n{jerr}')
        print()
        print(f'Input\n{test}')
        exit()
    tests[f'large-test-{i}'] = {'input':test, 'output':python}

# pprint(tests)
with open('tests.json', 'w+') as f:
    json.dump(tests, f, indent=4)
