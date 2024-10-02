# User function Template for python3

class Solution:
    # Function to reverse the queue.
    def rev(self, q):

        stack = []
        while not q.empty():
            stack.append(q.queue[0])
            q.get()

        while len(stack) > 0:
            q.put(stack[-1])
            stack.pop()

        return q
