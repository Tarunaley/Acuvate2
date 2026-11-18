s = "babad"
t=""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        subarry=s[i:j]

        rev=""
        for k in range(len(subarry)-1,-1,-1):
            rev+=subarry[k]
        # print(rev)
        if subarry==rev:
            if len(subarry) > len(t):
                t=subarry
print(t)



