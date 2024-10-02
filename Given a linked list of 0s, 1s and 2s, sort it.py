class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):

        zero = 0
        one = 0
        two = 0

        temp = head

        while temp != None:
            if temp.data == 0:
                zero += 1
            elif temp.data == 1:
                one += 1
            else:
                two += 1
            temp = temp.next

        temp = head

        while temp != None:
            if zero != 0:
                temp.data = 0
                zero -= 1

            elif one != 0:
                temp.data = 1
                one -= 1

            else:
                temp.data = 2
                two -= 1

            temp = temp.next

        return head