class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=dict()
        result=[]
        arr=[[] for _ in range(len(nums)+1)]
        for n in nums:
            if n not in count:
                count[n]=1
            else:
                count[n]+=1
        
        for key,value in count.items():
            arr[value].append(key)
        
        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                result.append(n)
                if len(result)==k:
                    return result



        

