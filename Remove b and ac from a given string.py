class Solution:
    def stringFilter(self, str):
        str = str.replace('ac', '')
        str = str.replace('b', '')
        return str