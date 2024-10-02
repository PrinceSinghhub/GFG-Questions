def reaching_height (n, arr) :
   #Complete the function
   arr.sort()
   lst=[]
   if(arr.count(arr[0])==n and n>1):
       return [-1]
   else:
       for i in range(0,n//2):
           x=i+1  #for accessing the last element which is highest
           lst.extend([arr[-x],arr[i]])
       if(n%2 != 0): # checking whether given no.of is even or odd
           lst.append(arr[n//2])  #adding the element
       return lst