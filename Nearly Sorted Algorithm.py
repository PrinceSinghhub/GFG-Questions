for i in range(int(input())):
   n,k=map(int,input().split())
   arr=list(map(int,input().split()))
   arr.sort()
   print(*arr)