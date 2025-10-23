class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            new=[]
            for i in range(len(s)-1):
                sum=(int(s[i])+int(s[i+1]))%10
                new.append(str(sum))
            s=''.join(new)
        return s[0]==s[1]