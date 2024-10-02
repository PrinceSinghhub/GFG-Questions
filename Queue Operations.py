# User function Template for python3
class Solution:
    # Function to insert element into the queue
    def insert(self, q, k):
        q.append(k)

    # Function to find frequency of an element
    # return the frequency of k
    def findFrequency(self, q, k):
        if k not in q:
            return -1

        return q.count(k)
        # code here
