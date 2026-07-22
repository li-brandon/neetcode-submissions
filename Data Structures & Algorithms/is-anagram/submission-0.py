class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_s = {}
        for i in s:
            if i not in letters_s:
                letters_s[i] = 1
            else:
                letters_s[i] += 1
        
        letters_t = {}
        for j in t:
            if j not in letters_t:
                letters_t[j] = 1
            else:
                letters_t[j] += 1
        
        return True if letters_s == letters_t else False