class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        left=0
        right=len(heights)-1
        while left<right:
            height= min(heights[left], heights[right])
            width=right-left
            area= height*width
        
            if area>max:
                max=area
            
            if heights[left]>heights[right]:
                right-=1
            elif heights[left]<heights[right]:
                left+=1
            elif heights[left]==heights[right]:
                right-=1
                left+=1
        return max
