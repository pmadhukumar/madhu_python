class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(path, remaining):
            # If no more numbers to add, we have a complete permutation
            if not remaining:
                res.append(path)
                return
            for i in range(len(remaining)):
                # Choose the i-th number and explore further
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return res

# Example usage:
sol = Solution()
print(sol.permute([1, 2, 3]))
