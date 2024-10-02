def findMissing(A,B,N,M):

    ans = []
    for i in A:
        if i in B:
            # B.remove(i)
            continue
        else:
            ans.append(i)

    for j in ans:
        return str(j)


t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ans=findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# a = [225, 17, 18, 20 ,11, 20, 25, 7 ,27, 11, 22, 21, 22, 10, 13, 12, 9, 9, 28, 28, 20, 2, 2, 26, 3, 27]
# b = [27,33, 19, 26, 20, 32, 17, 38, 25, 31, 18, 18, 32, 24, 28, 11, 35, 29]
# 26 18
# 225 17 18 20 11 20 25 7 27 11 22 21 22 10 13 12 9 9 28 28 20 2 2 26 3 27
# 27 33 19 26 20 32 17 38 25 31 18 18 32 24 28 11 35 29
#
#
# 225 7 22 21 22 10 13 12 9 9 2 2 3

# # for i in a:
#     if i in b:
#         b.remove(i)
#         continue
#     else:
#         print(i,end=" ")

