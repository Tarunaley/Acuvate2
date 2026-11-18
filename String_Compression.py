class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res=""
        i=0
        while(i<len(chars)):
            count=1
            for j in range(i+1,len(chars)):
                if(chars[i]==chars[j]):
                    count+=1
                else:
                    break
            if(count>1):
                res+=chars[i]+str(count)
            else:
                res+=chars[i]
            i+=count
        for k in range(len(res)):
            chars[k]=res[k] 
        
        return len(res)
