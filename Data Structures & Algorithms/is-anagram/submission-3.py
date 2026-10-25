class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        d = {}
        for letter in s:
            if letter not in d:
                d[letter] = 0
            d[letter] += 1
        
        for letter in t:
            if letter not in d or d[letter] == 0:
                return False
            else:
                d[letter] -= 1
        
        return True
        