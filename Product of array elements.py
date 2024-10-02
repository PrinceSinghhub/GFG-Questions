def product(arr, n, mod):
    ans = 1

    for i in arr:
        ans *= i
    return ans % mod


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    mod = 1000000007
    for j in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(product(arr, n, mod))