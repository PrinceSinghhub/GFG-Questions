# Your task is to complete this function
# Your shouldn't return any thing it should print the required output
def addFraction(num1, den1, num2, den2):
    import math
    nums = num1 * den2 + num2 * den1
    dens = den1 * den2
    gcd = math.gcd(nums, dens)
    print(str(int(nums / gcd)) + "/" + str(int(dens / gcd)))


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split(' ')))

        addFraction(arr[0], arr[1], arr[2], arr[3])