class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1={}
        max1=0
        i=1
        curr=1
        k1=k
        curr_ele=s[0]
        while (i<len(s)):
            if(s[i]!=curr_ele):
                if(s[i] not in dict1):
                    dict1[s[i]]=i
                k1-=1
            if(k1==-1):
                for value in dict1.values():
                    i=value
                    curr_ele=s[i]
                    curr=0
                    break
                k1=k
                dict1.clear()
                continue
            curr+=1
            max1=max(max1,curr)
            i+=1
        if(k1!=0 and curr!=len(s)):
            curr=min(curr+k1,len(s))
        return max(max1,curr)