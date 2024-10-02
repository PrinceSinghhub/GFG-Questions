def num(arr, n, k):
    count = 0

    for i in arr:
        con = str(i)
        count += con.count(str(k))
    return count
    # Code here

print(num([11,12,13,14,15],5,1))