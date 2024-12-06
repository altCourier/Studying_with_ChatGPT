# If we XOR two same values A XOR A =  0
# So if we just XOR elements starting from 1 to n
# The num that doesnt get 0 is the missing value.

arr = [1,2,3,4,6,7,8]
def missingNumber(arr, n):
    result = 0
    for num in range(1, n+1):
        result ^= num
    for num in arr:
        result ^= num
    return result

print(missingNumber(arr, 8))
