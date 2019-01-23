# Atuhor:ZJF
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea=0
        pointer_left=0
        pointer_right=len(height)-1
        while pointer_left != pointer_right:
            l=height[pointer_left]
            r=height[pointer_right]
            area = (pointer_right-pointer_left)*min(l,r)
            if area>maxarea:
                maxarea=area
            if l>r:
                pointer_right -= 1
            else:
                pointer_left += 1
        return maxarea