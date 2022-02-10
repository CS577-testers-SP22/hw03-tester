#Build commands to copy:
#Replace g++ -o HelloWorld HelloWord.cpp below with the appropriate command.
#Java:
# javac source_file.java
#Python:
# echo "Nothing to compile."
#C#:
# mcs -out:exec_name source_file.cs
#C:
# gcc -o exec_name source_file.c
#C++:
# g++ -o exec_name source_file.cpp
build:
	g++ -o Scheduling Scheduling.cpp
#Run commands to copy:
#Replace ./HelloWorld below with the appropriate command.
#Java:
# java source_file
#Python 3:
# python3 source_file.py
#C#:
# mono exec_name
#C/C++:
# ./exec_name
run:
	./Scheduling

clean:
	rm ./Scheduling
