class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for i in s:
            if i.isalnum():
                clean += i.lower()

        if list(clean) == list(reversed(clean)):
            return True
        return False
        