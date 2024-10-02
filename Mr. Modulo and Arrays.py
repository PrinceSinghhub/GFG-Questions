import bisect


def maxModValue(arr, n):
    ans = 0

    # Sort the array[] by using inbuilt
    # sort function
    arr = sorted(arr)

    for j in range(n - 2, -1, -1):

        # Break loop if answer is greater or equals to
        # the arr[j] as any number modulo with arr[j]
        # can only give maximum value up-to arr[j]-1
        if (ans >= arr[j]):
            break

        # If both elements are same then skip the next
        # loop as it would be worthless to repeat the
        # rest process for same value
        if (arr[j] == arr[j + 1]):
            continue
        i = 2 * arr[j]
        while (i <= arr[n - 1] + arr[j]):
            # Fetch the index which is greater than or
            # equals to arr[i] by using binary search
            # inbuilt lower_bound() function of C++
            ind = bisect.bisect_left(arr, i)
            # Update the answer
            ans = max(ans, arr[ind - 1] % arr[j])
            i += arr[j]

    return ans


# {
#  Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    print(maxModValue(a, n))

# } Driver Code Ends