class Solution:
    def compareFrac(self, s):
        # Split the string and trim spaces
        store = s.split(", ")

        # Convert the fractions to float values for comparison
        frac1 = eval(store[0])
        frac2 = eval(store[1])

        # Compare the float values of the fractions
        if frac1 > frac2:
            return store[0]
        elif frac1 == frac2:
            return "equal"
        else:
            return store[1]