'''
Tests for UW Madison CS577 Spring 2022 LEC 002 (Marc's section)

HW03: Greedy Algorithms
'''

__maintainer__ = 'CS577-testers-SP22'
__author__ = ['Nicholas Beninato']
__version__ = '1.0'

import difflib
import json
import sys

from pprint import pprint
from subprocess import Popen, PIPE
from time import time
from urllib.request import urlopen

try:
    from tqdm import tqdm
except ModuleNotFoundError as e: # don't have tqdm installed
    import shutil
    def tqdm(iterable):
        '''discount tqdm progress bar'''
        width = shutil.get_terminal_size().columns
        for i, x in enumerate(iterable):
            itr = (i + 1)
            percent = f'{int(itr / len(iterable)*100):>3}'
            end = '\r' if i != len(iterable) - 1 else '\n'
            before = f'{percent}% '
            after = f' {" " * (len(str(len(iterable))) - len(str(itr)))}{itr} / {len(iterable)}'
            available = (width - len(before + after)) - 2
            bar = '[' + (int(available * itr/len(iterable)) - 1) * '=' + '>' * (end == '\r')
            bar = bar + ' ' * (available - len(bar)) + ']'
            print(f'{before}{bar}{after}', end=end)
            yield x

TEST_FILE = 'tests.json'

test_output = []
test_cases = []

def timeit(func):
    def timed_func(*args, **kwargs):
        t0 = time()
        out = func(*args, **kwargs)
        runtime = f'{(time() - t0)*1000:.2f}'
        test_output.append(f'PASSED {func.__name__}{" "*(21-len(func.__name__))} in {(runtime):>8} ms')
        return out
    test_cases.append(timed_func)
    return timed_func

def shell(cmd, stdin=None):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    out, err = p.communicate(input=stdin.encode() if stdin else None)
    return out.decode('utf8'), err.decode('utf8')

@timeit
def test1_build():
    print('Building:')
    buildOutput, buildError = shell('make build')
    if buildOutput:
        print(buildOutput)
    if buildError:
        print('Error running `make build`:\n')
        print(buildError)
        exit()

@timeit
def test2_open_test_file():
    try:
        with open(TEST_FILE, 'r') as f:
            tests = json.load(f)
    except FileNotFoundError as e:
        print(f'Unable to open {TEST_FILE}. Please check it is in the same directory.')
        exit()
    
    return tests

@timeit
def test3_canvas_tests(tests):
    print('Running Canvas Tests')
    subset = {k:v for k,v in tests.items() if k.startswith('canvas')}

@timeit
def test4_small_tests(tests):
    print('Running Small Tests')
    run_tests({k:v for k,v in tests.items() if k.startswith('small')})

@timeit
def test5_medium_tests(tests):
    print('Running Medium Tests')
    run_tests({k:v for k,v in tests.items() if k.startswith('medium')})

@timeit
def test6_large_tests(tests):
    print('Running Large Tests')
    run_tests({k:v for k,v in tests.items() if k.startswith('large')})

def run_tests(tests):
    for testName, testCase in tqdm(tests.items()):
        userOutput, userError = shell('make run', stdin=testCase['input'])
        userOutput = '\n'.join(userOutput.split('\n')[1:]) # first line is Makefile's run command
        if userOutput != testCase['output']:
            print(f"Failed test: {testName}")
            print(f"Input:\n{testCase['input']}\n")
            print(f"Expected output:\n{'*'*32}\n{testCase['output']}\n{'*'*32}\n")
            print(f"Program output:\n{'*'*32}\n{userOutput}\n{'*'*32}\n")
            if len(userError) > 1:
                print(f"Program error:\n{userError}")

            diff = list(difflib.ndiff(userOutput, testCase['output']))
            whitespace = {'\n':'"\\n" (newline)', '\t':'"\\t" (tab)', ' ':'" " (space)'}

            if any(x[0] != ' ' and x[-1] in whitespace for x in diff):
                print('Whitespace difference between user and expected outputs:')
                for i,s in enumerate(diff):
                    if s[0] == ' ' or s[-1] != '\n': continue
                    elif s[0] == '-':
                        print(f'Extra {whitespace[s[-1]]} at position {i}')
                    elif s[0] == '+':
                        print(f'Missing {whitespace[s[-1]]} at position {i}')
                print()
            if not all(x[0] == ' ' or x[-1] in whitespace for x in diff):
                print("Output difference (lines with - need to be removed, lines with + need to be added):")
                sys.stdout.writelines(difflib.unified_diff(userOutput.splitlines(keepends=True), 
                                                           testCase['output'].splitlines(keepends=True), 
                                                           fromfile='Program Output', 
                                                           tofile='Expected Output'))
            exit()

def main():
    test1_build()
    tests = test2_open_test_file()
    test3_canvas_tests(tests)
    test4_small_tests(tests)
    test5_medium_tests(tests)
    test6_large_tests(tests)

def get_versions():
    current = __version__
    to_tuple = lambda x: tuple(map(int, x.split('.')))
    try:
        with urlopen('https://raw.githubusercontent.com/CS577-testers-SP22/hw03-tester/master/.version') as f:
            if f.status != 200:
                raise Exception
            latest = f.read().decode('utf-8')
    except Exception as e:
        print('Error checking for latest version.') # very descriptive error messages
        return to_tuple(current), to_tuple(current) # ignoring errors is good practice
    return to_tuple(current), to_tuple(latest)

if __name__ == '__main__':
    print(f'Running CS577 SP22 HW03 tester v{__version__}')

    current, latest = get_versions()
    to_v_str = lambda x : '.'.join(map(str, x))
    if current < latest:
        print(f'A newer version of this tester (v{to_v_str(latest)}) is available. You are current running v{to_v_str(current)}\n')
        print('You can download the latest version at https://github.com/CS577-testers-SP22/hw03-tester\n')
    print()
    main()
    print()
    for message in test_output:
        print(message)
    print()
    print('Passed all tests successfully.')
