class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq_dict={}
        for i,val in enumerate(nums):
            if val-1 not in nums:
                seq_dict[val]=[val]
        max=0
        for key,val in seq_dict.items():
            while val[-1]+1 in nums:
                val.append(val[-1]+1)
            if len(val)>max:
                max=len(val)


        return max