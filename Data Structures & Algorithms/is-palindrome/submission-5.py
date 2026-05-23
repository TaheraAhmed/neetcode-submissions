class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res=True
        clean_string=""
        #clean_text = "".join(char for char in s if char.isalnum())
        for i in range(len(s)):
            if s[i].isalnum():
                clean_string=(clean_string+s[i]).lower()
        start=0
        end=len(clean_string)-1

        if clean_string=='':
            return res
        while start!=end:
            if clean_string[start]==clean_string[end]:
                start+=1
                end-=1  
                if start>end:
                    break  
            else:
                res=False
                return res
        
        return res
                
             
            