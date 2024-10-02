class Solution:


    def matchPairs(self, n, nuts, bolts):


        # code her
        l = ["!", "#", "$", "%", "&", "*", "?", "@", "^"]
        for i in range(len(l)):
            if l[i] in nuts and l[i] in bolts:
                nuts.remove(l[i])
                nuts.append(l[i])
                bolts.remove(l[i])
                bolts.append(l[i])

        return ("".join(nuts))
        return ("".join(bolts))