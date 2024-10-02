def rotate(matrix):
    ans = []

    for i in range(len(matrix) - 1, -1, -1):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])

        ans.append(temp)

    return ans

arr = [[1,2, 3],
              [4, 5 ,6],
              [7 ,8 ,9]]
print(rotate(arr))