# Fibonacci-

This is a python program that determines the term of the Fibonacci sequence in which N amount of digits are present where the user inputs the number N.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CODE RUNDOWN
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The code of the program starts by importing the numpy library as well as the sys. The numpy library is used to do mathematical calculations and sys is imported in order for the input to be read using an entry point in the dockerfile.

The fibonacci sequence starts with two terms both equal to 1, thus meaning that Term_1 = 1 and Term_2 = 1. The rest of the terms are determined by summing the previous 2 terms. It is therefore necessary to initialise the first 2 terms in an array which will also store the terms to follow.

The user input is recorded using the sys.argv[] function needed for the entry point specified in the docker file. The user input should consist of a unsigned integer and should specify the amount of digits that should be in the term.

The variable responsible for keeping track of the term number is the index variable and the variable responsible for storing the size/digit amount is the size variable. The index variable starts at 2 as the first 2 terms are known and present in the array.

The main calculations of determining the next terms of the sequence as well as determining the amount of digits of each of the terms while testing whether it is equal to the user input takes place in a while loop. The loop is set to run while the size variable and the user input are not the same. The next term of the sequence is calculated and is appended to the existing array. The amount of digits in the term is then mathematically calculated using the following equation: size = log10(x) + 1.
Note that the answer obtained from the equation needs to be rounded down to the integer therefore if the answer was 1.6 it would be rounded to 1. This is achieved by using the np.floor function from the numpy library. For every iteration of the while loop the index is incremented by 1.

Lastly the results is then printed for the user to see.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
