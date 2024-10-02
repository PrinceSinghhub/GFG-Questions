def formatArray(a,n):
    # add code here
    for i in range(0,n-1,2):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    #print(a)
    return a