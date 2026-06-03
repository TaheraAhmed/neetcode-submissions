class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum=0
        left=0
        right=len(heights)-1
        while left<right:
            height= min(heights[left], heights[right])
            width=right-left
            area= height*width

            maximum=max(area,maximum)
            
            if heights[left]>heights[right]:
                right-=1
                continue
            elif heights[left]<heights[right]:
                left+=1
                continue
            elif heights[left]==heights[right]:
                right-=1
                left+=1
                continue
        return maximum
