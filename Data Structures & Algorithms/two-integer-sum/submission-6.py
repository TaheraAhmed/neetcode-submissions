class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for i,val in enumerate(nums):
            prevMap[val]=i
        
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in nums and i!=prevMap[diff]:
                return [i,prevMap[diff]]
                


      
    
