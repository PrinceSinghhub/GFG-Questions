def multiply(arr):
    first = arr[0:len(arr) // 2]
    second = arr[len(arr) // 2::]

    return sum(first) * sum(second)


arr = [1,2,3,4,5,6]
print(multiply(arr))

