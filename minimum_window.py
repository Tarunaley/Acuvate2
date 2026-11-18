class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isContains(word):
            for i in t:
                if word.count(i)<t.count(i):
                    return False
            return True
        n = len(s)
        res = ""
        mini = float('inf')
        for i in range(len(s)):
            substring=""
            j = i
            while j<n:
                substring += s[j]
                if len(substring)>=len(t) and isContains(substring):
                    if len(substring)<mini:
                        mini = len(substring)
                        res = substring
                j+=1
        return res
