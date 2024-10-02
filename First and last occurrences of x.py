def findIndex(arr, x, boll):
    start = 0
    end = len(arr) - 1

    ans = -1

    while start <= end:
        mid = start + (end - start) // 2

        if x > arr[mid]:
            start = mid + 1

        if x < arr[mid]:
            end = mid - 1

        if x == arr[mid]:
            ans = mid

            if boll == True:
                end = mid - 1

            else:
                start = mid + 1

    return ans


def find(arr, n, x):
    # code here

    ans = [-1, -1]

    start = findIndex(arr, x, True)
    end = findIndex(arr, x, False)

    ans[0] = start
    ans[1] = end

    return ans


# {
#  Driver Code Starts
t = int(input())
for _ in range(0, t):
    l = list(map(int, input().split()))
    n = l[0]
    x = l[1]
    arr = list(map(int, input().split()))
    ans = find(arr, n, x)
    print(*ans)