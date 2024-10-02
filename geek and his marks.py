n=int(input())
for i in range(n):
    student, geeks = map(int, input().split())
    t=list(map(int,input().split()))
    result=0
    for k in t:
        if k>geeks:
            result+=1

    print(result)