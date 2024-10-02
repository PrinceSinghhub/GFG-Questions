def max_sum(a,n):
    #code here
    arr_sum = 0
    curr_val = 0

    for i in range(0, n):
        arr_sum = arr_sum + arr[i]
        curr_val = curr_val + (i*arr[i])

    max_val = curr_val

    for j in range(1, n):
        curr_val = curr_val + arr_sum - n * arr[n-j]
        if (curr_val > max_val):
            max_val = curr_val

    return max_val