def check(arr, brr, n):
    arr.sort()
    brr.sort()

    if len(arr) != len(brr):
        return 0

    for i in range(n):
        if arr[i] == brr[i]:
            continue
        else:
            return 0
    return 1

arr = [1, 2, 3, 4, 5]
brr = [3, 4, 1, 2, 5]
print(check(arr,brr,len(arr)))