def chocolates(arr, n):
    # Complete the function
    # return min(arr)

    i = 0
    j = n - 1
    while i < j:
        if arr[i] <= arr[j]:
            j -= 1
        else:
            i += 1
    return arr[j]