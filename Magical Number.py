def binarySearch(arr, low, high):
    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] > mid:
            high = mid - 1

        elif arr[mid] < mid:
            low = mid + 1

        else:
            return mid

    return -1

arr = [0,1,2,3,4,5,6,7,8,9]
print(binarySearch(arr,0,len(arr)-1))