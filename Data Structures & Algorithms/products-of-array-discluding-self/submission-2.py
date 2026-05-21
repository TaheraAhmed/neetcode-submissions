class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        
        for i in range(len(nums)):
            suffix_prod=1
            j=i+1
            while j<len(nums):
                suffix_prod=suffix_prod*nums[j]
                j=j+1
            
            suffix[i]=suffix_prod
        
        for i in range((len(nums)-1),0,-1):
            prefix_prod=1
            j=i-1
            while j>=0:
                prefix_prod=prefix_prod*nums[j]
                j=j-1
            
            prefix[i]=prefix_prod
        
        res=[suffix[i]*prefix[i] for i in range(len(nums))]

        return res


      


            