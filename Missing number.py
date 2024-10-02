# User function Template for python3

def missingNumber(A, N):
    return sum(list(range(N + 1))) - sum(A)

    # bruteforce Approch
    # for i in range(1,N+1):
    #     if i in A:
    #         continue
    #     else:
    #         return i
    #  # Your code goes here

print(missingNumber([1,3,4,5],5))