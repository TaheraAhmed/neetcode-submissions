class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res=True
        # clean_string=""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         clean_string=clean_string+(s[i].lower())
        start=0
        end=len(s)-1
        # if s=='':
        #     return res
        s=s.lower()
        while start!=end: 
            if s[start].isalnum()==False:
                start+=1
                continue
            if s[end].isalnum()==False:
                end-=1
                continue
            if s[start]==s[end]:
                start+=1
                end-=1  
                if start>end:
                    break  
            else:
                res=False
                return res
        
        return res



        
                
             
            