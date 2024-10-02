def game_with_number (arr,  n) :
   #Complete the function
   result = []
   start = 1
   while start <=n:
       if start == n:
           result.append(arr[start-1])
           break
       t = arr[start-1] ^ arr[start]
       result.append(t)
       start +=1
   return result