class Solution:
   def closestPalindrome(self, num):
       k=str(num)
       l=[]
       o=num
       dict={}
       counter=0
       if(k==k[::-1]):
          return num
       for i in range (0,100000000):
           o=o+1
           counter=counter+1
           if str(o)==str(o)[::-1]:
               l.append(o)
               l.append(counter)
               #dict.setdefault(o,counter)
               break
       o=num
       counter=0
       for i in range (0,1000000000):
           o=o-1
           counter=counter+1
           if str(o)==str(o)[::-1]:
               l.append(o)
               l.append(counter)
               #dict.setdefault(o,counter)
               break
       if l[1]==l[-1]:
           if(l[0]>l[2]):
               return l[2]
           else:
               return l[0]
       if l[1]<l[-1]:
           return l[0]
       else:
           return l[2]