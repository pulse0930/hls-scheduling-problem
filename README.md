# hls-scheduling-problem
Scheduling in High Level Synthesis.CAD for VLSI problem


1.PROJECT STRUCTURE:
---------------------------------------------------------
+hls-scheduling
	+lpsolverfiles					
		-lpinput.lp
		-lpoutput.txt
	+testcases
		+tc1
			-input.txt
		+tc2
			-input.txt
		+tc3
			-input.txt
		+tc4	
			-input.txt	
	+scheduler
		-__init__.py	
		-module_file.py
		-module_graph.py
		-module_ILP.py
	-iotest.txt
	-readme.txt	
	-scheduler.py
			

+lpsolverfiles
It's a directory holding lp solver input and output files which are created on executing the program.

+testcases
It's directory for testcases.Under this tc1,tc2... are testcase directories having test input files as 'input.txt'

+scheduler
It's a package used by the program. Under this 3 modules are:
-module_file.py
	class FileIO  consists of methods for reading writing file operations. 
-module_graph.py
	class OCG modelling the OCG graph properties such as operation properties represented as node/vertex ,dependencies of each operation represented as edges.
-module_ILP.py
	class ILPmodeller consists of methods for generating the data required for solving. 

-iotest.txt
input and output for the test cases in testcases directory.

-scheduler.py
Main program. Instructions for executing this program is in section 3. 


2.INPUT:
---------------------------------------------------------
An example of input file is given below:
adjmat:
0	1	1	1	0	0	0	0
0	0	0	0	1	0	0	0
0	0	0	0	0	1	1	0
0	0	0	0	0	0	0	1
0	0	0	0	0	1	0	0
0	0	0	0	0	0	1	0
0	0	0	0	0	0	0	1
0	0	0	0	0	0	0	0
rtype:
0	1	1	3	2	2	1	0
di:
1	2	2	1	1	1	2	1
ak:
1	1	1	1
lambda:
6

1. 1st part of input file is the adjacency matrix of the ocg graph
2. 2nd part is the resource type for each operation 
3. 3rd part is the delay propagation for each operation (Considering delay propagation for operations using same resources will be same)
4. 4th part is the upper bound of the number of resources for resource type k
5. 5th part is the Lambda value

NOTE:
INPUT FILES MUST BE SAVED AS input.txt

3.TO EXECUTE:
---------------------------------------------------------
Help command:
	python scheduler.py -h
NOTE: 
help docs are not available now.

Syntax for executing:
	python scheduler.py -p <input-file-path>
	NOTE:	
	-p indicates argument for path 
	
Example.From terminal type this command:
	python scheduler.py -p testcases/tc1/

NOTE:
The above command is will take the input.txt located in the path 'testcases/tc1/' as an input 
Similarly you can check for another input:tc2 'testcases/tc2/'

4.OUTPUT:
---------------------------------------------------------
The output will be stored as 'output.txt' in the path where the input file 'input.txt' is located.

5.DETAILED DESCRIPTION
---------------------------------------------------------
The program scheduler.py takes command line input which is the path of the 'input.txt' file. From this path the program reads the 'input.txt' extracts the 5 inputs (adjacency matrix, resource type for each operation, delay propagation for each operation, number of resources for a resource type and lambda value) from the file.

Then an object of OCG class is created initializing the class variables.(Parameterized constructor __init__ called passing the 5 inputs as arguments)

Then an object of ILPmodeller class is created initializing the class variables.Parameterized constructor __init__ called passing the object of OCG as argument)

Then resource_constraint() method of ILPmodeller class is called. This method returns input data (as string data type) for the lp_solver program.

This input data is written in 'lpinput.lp' file which serves the input to the lp_solver program.

"lp_solve lpinput.lp > lpoutput.txt" shell command is executed from the program.

So now the 'lpoutput.txt' is holding the lpsolver output.

Now X variables having value 1 are extracted from lpoutput.txt file and then they are interpreted into meaningfull results which are written in 'output.txt' file. 
