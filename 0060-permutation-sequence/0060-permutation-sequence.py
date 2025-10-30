class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        
        # Initialize numbers 1 to n
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert k to 0-indexed
        result = []
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result.append(numbers.pop(index))
            k %= fact
        
        return ''.join(result)

# Example usage:
sol = Solution()
print(sol.getPermutation(3, 3))  # Output: "213"
print(sol.getPermutation(4, 9))  # Output: "2314"
