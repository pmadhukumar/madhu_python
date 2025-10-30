class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Convert integer to string and compare with reverse
        str_x = str(x)
        return str_x == str_x[::-1]

# Example usage:
sol = Solution()
print(sol.isPalindrome(121))  # True
print(sol.isPalindrome(-121)) # False
print(sol.isPalindrome(10))   # False
