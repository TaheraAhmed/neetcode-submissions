class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs=''
        for string in strs:
            m=len(string)
            new_string=str(m)+'#'+ string
            new_strs=new_strs+new_string
        
        return new_strs

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]

        while i < len(s):
            j=i
            while s[j]!='#':
                j=j+1
            length=int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j

        return res