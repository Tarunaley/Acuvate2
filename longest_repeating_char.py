def char_repeating(s,k):
    left=0
    max_length=0
    for right in range(len(s)):
        count=0
        for i in range(left,right+1):
            if s[i]==s[right]:
                count+=1
        length=right-left+1
        if length-count<=k:
            max_length=max(max_length,length)
        else:
            left+=1
    return max_length
s="ABAB"
k=2
print(char_repeating(s,k))
                