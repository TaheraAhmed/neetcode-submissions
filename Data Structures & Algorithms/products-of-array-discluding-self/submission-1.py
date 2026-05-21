class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]*len(nums)
        for i in range(len(nums)):
            prod=1
            for j in range(i):  
                prod=prod*nums[j]
            pref[i]=prod
        suff=[1]*len(nums)
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)-1,i,-1):  
                prod=prod*nums[j]
            suff[i]=prod
        
        res=[pref[i]*suff[i] for i in range(len(nums))]
        return res
        
