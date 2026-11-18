class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        if len(s1)==1:
            if s1 in s2:
                return True
            return False
        s1=sorted(s1)
        i=0
        j=len(s1)
        while j<=len(s2):
            a=sorted(s2[i:j])
            if a==s1:
                return True
            i+=1
            j+=1
        return False