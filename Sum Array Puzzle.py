def SumArray(arr, n):

    # fast code
    # arr = list(map(int, arr))
    # s = sum(arr)
    # for i in arr:
    #     print(s - i, end=" ")
    ans = []

    for i in range(n):
        temp = 0
        for j in range(n):
            if i == j:
                continue
            else:
                temp += arr[j]
        ans.append(temp)
    return ans

print(SumArray([3,6,4,8,9],5))