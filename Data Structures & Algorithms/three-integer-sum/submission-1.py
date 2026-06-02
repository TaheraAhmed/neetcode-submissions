class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums_sorted=sorted(nums)
        for i in range(len(nums_sorted)):
            left= i
            right= len(nums_sorted)-1
            next= i+1
            while next<right:
                if nums_sorted[left]+nums_sorted[right]+nums_sorted[next]==0:
                    res.append([nums_sorted[left],nums_sorted[right],nums_sorted[next]])
                    right-=1
                    next+=1
                if nums_sorted[left]+nums_sorted[right]+nums_sorted[next]<0:
                    next+=1
                    
                if nums_sorted[left]+nums_sorted[right]+nums_sorted[next]>0:
                    right-=1
                    
        final=[]
        for i in res:
            if i not in final:
                final.append(i)
        return(final)