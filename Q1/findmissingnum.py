# You are given an array of n - 1 integers in the range from 1 to n. The array contains no duplicates, 
# and one of the numbers in the range from 1 to n is missing.
# Write a function to find the missing number.

# arr = [1, 2, 4, 6, 3, 7, 8]
# n = 8
# output: 5

def find_missing_num(arr: list[int], n:int) -> int:
    return (n*(n+1) / 2) - sum(arr)

find_missing_num([1, 2, 4, 6, 3, 7, 8], 8)