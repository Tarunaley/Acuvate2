class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=""
        
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
             
                ans=s[i:j+1]
                if len(ans)==len(set(ans)):
                    if len(ans)>len(longest) :
                        longest=ans
                    
        return len(longest)
        