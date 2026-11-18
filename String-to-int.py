class Solution:
    def myAtoi(self, s: str) -> int:
        k=""
        for i in range(len(s)):
            if s[i]==' ':
                continue
            elif s[i]=='-' and (i==0 or s[i-1]==' '):
                k=k+s[i]
            elif s[i]=='0' and s[i-1]=='-':
                continue
          
            elif not s[i].isdigit():
                break
            else:
                k=k+s[i]
                
        if len(k)>0:
            return int(k)
        else:
            return 0
