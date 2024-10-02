def uniqueRow(row, col, matrix):
    ans = []
    for i in range(0, len(matrix), col):
        cr = "".join(matrix[i:i + col])
        if cr not in ans:
            ans.append(cr)
    return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    testcase = int(input())
    while (testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = input().split()

        a = uniqueRow(row, col, matrix)

        for row in a:
            for value in row:
                print(value, end=" ")
            print("$", end="")
        print()
        testcase -= 1


if __name__ == "__main__":
    main()