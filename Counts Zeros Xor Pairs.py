def calculate(arr, n):
    # Complete the function
    count = 0

    for i in range(n):
        for j in range(i + 1, n):

            if arr[i] ^ arr[j] == 0:
                count += 1

    return count


# {
#  Driver Code Starts
# Initial Template for Python 3

for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = calculate(arr, n)
    print(res)