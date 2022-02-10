# hw03-tester

Additional tests for CS577 Spring 2021 HW03: Greedy Algorithms

## Changes

### V1.0
 - Initial commit

## Downloading

### Option 1: Clone the entire repo

 - Run `$ git clone https://github.com/CS577-testers-SP22/hw02-tester/`
 - Copy your code and `Makefile` into the repo

### Option 2: Download specific files

 - Download [tests.json](tests.json) and [hw03-test.py](hw03-test.py) into the directory that contains your `Makefile` and code. Your need to be able to run your code using `$ make build && make run` in that directory.

## Usage

The contents of your directory should look like this:

```shell
.
├── Makefile
├── source_code
├── tests.json
└── hw03-test.py
```

where `source_code` is the file(s) you'd submit to Gradescope with your `Makefile`. Mine is `Scheduling.cpp`, but you might have `hw03.py`, `Main.java`, or something else.

To run the tests, do

```shell
$ python3 hw03-test.py
```

`tqdm` is used to track progress. If you don't have it installed, you should do `$ pip install tqdm`.

## Additional Information

 - If you want to see how the tests were generated, or generate your own, see [generate_tests.py](generate_tests.py)
 - These are not the actual tests Gradescope uses. I just generated random inputs that meet the specified requirements for input, and made sure the outputs matched for a few different languages that each passed all Gradescope tests.

## Disclaimer

These tests are not endorsed or created by anyone working in an official capacity with UW Madison or any staff for CS577. The tests are make by students, for students.

By running any of the code in this repository, you are executing code you downloaded from the internet. Back up your files and take a look at what you are running first.

If you have comments / questions / suggestions, create an [issue](/../../issues) or ask in the Discord at [https://discord.gg/CTFKYaUePf](https://discord.gg/CTFKYaUePf). If you want to contribute, submit a pull request or ask to join the organization in Discord.