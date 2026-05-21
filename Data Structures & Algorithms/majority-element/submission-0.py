class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        all_nums={}
        for i,v in enumerate(nums):
            all_nums[v]=1 + all_nums.get(v,0)
        
        n=len(nums)
        x=int(n//2)

        for key,val in all_nums.items():
            if val>x:
                return key