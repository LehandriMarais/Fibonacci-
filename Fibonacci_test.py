# fibonacci sequence program test environment

import numpy as np

fibonacci_arr = np.array([1, 1]) # This is the Array which will contain the fibonacci sequence with the first 2 terms already entered

in_put =  int(input("Enter the amount of digits: "))

size = 0
index = 2  # Index set to 2 as the first 2 terms are already known and in the array

while size != in_put:
    # Calculate next term of sequence
    # ----------------------------------------------------------
    add = np.add(fibonacci_arr[index-1], fibonacci_arr[index-2])
    fibonacci_arr = np.append(fibonacci_arr, add)
    #-----------------------------------------------------------

    # Mathmatically calculate the number of digits in the current term
    size = np.floor(np.add(np.log10(add), 1))

    index = np.add(index, 1)

print("The first index with " + str(size) + " digits is: " + str(index))

# For testing purposes
# print("The fibonacci sequence is:")
# print(fibonacci_arr)
