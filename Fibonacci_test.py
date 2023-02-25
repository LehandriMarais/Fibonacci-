# fibonacci sequence program test environment

import sys
import numpy as np

fibonacci_arr = np.array([1, 1]) # This is the Array which will contain the fibonacci sequence with the first 2 terms already entered

in_put = int(sys.argv[1])

size = 0
index = 2  # Index set to 2 as the first 2 terms are already known and in the array

while size != in_put:
    # Calculate next term of sequence
    # ----------------------------------------------------------
    adds = np.add(fibonacci_arr[index-1], fibonacci_arr[index-2])

    fibonacci_arr = np.append(fibonacci_arr, adds)
    #-----------------------------------------------------------

    # Mathmatically calculate the number of digits in the current term
    size = np.floor(np.add(np.log10(adds), 1))

    index = np.add(index, 1)

print("The first index with " + str(in_put) + " digits is: " + str(index))

# For testing purposes
# print("The fibonacci sequence is:")
# print(fibonacci_arr)