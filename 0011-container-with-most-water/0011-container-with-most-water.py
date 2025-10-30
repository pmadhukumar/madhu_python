class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Width between the two lines
            width = right - left
            # Height is limited by the shorter line
            current_area = min(height[left], height[right]) * width
            # Update maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage:
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
