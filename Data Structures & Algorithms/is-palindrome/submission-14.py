import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum())
        print(cleaned)
        print(cleaned[::-1])
        return cleaned.lower() == cleaned[::-1].lower()