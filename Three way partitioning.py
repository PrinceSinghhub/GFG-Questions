class Solution:
    #Function to partition the array around the range such
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    array.sort()
	    return 1