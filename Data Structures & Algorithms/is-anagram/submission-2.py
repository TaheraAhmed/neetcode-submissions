class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count={}
        for i in range(len(s)):
            if s[i] not in s_count:
                s_count[s[i]]=1
            if s[i] in s_count:
                s_count[s[i]]+=1
        t_count={}
        for i in range(len(t)):
            if t[i] not in t_count:
                t_count[t[i]]=1
            if t[i] in t_count:
                t_count[t[i]]+=1


        if s_count==t_count:
            return True
        
        else:
            return False