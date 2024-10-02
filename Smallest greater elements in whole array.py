from bisect import bisect_right


def greaterElement(arr, n):
    sortedArr = sorted(arr[:])
    res = []
    for e in arr:
        idx = bisect_right(sortedArr, e)
        res.append(-10000000 if idx == n else sortedArr[idx])
    return res


# {
#  Driver Code Starts
# Initial Template for Python 3

for _ in range(0, int(input())):

    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = greaterElement(arr, n);
    ans = ""
    for i in res:
        if (i == -10000000):
            ans += "_ "
        else:
            ans += str(i) + " "
    print(ans)