class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            prefix=""
            return prefix
        strs.sort()
        prefix=strs[0]
        for word in strs[1:]:
            for c in word:
                if prefix in word:
                    continue
                else:
                    prefix=prefix[:-1]
        
        return(prefix)

        