from collections import OrderedDict

class Solution:
    def removeAllDuplicates(self, head):
        #code here
        temp=head
        di={}
        while(temp):
            if temp.data in di:
                di[temp.data]+=1
            else:
                di[temp.data]=1
            temp=temp.next
        dic1=OrderedDict(sorted(di.items()))
        new=Node(-1)
        temp1=new
        for i in dic1:
            if dic1[i]==1:
                p=Node(i)
                temp1.next=p
                temp1=p
        return new.next