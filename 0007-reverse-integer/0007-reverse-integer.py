class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        result = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x = x // 10
            
            # Check for overflow before multiplying by 10
            if result > (INT_MAX - digit) // 10:
                return 0
            
            result = result * 10 + digit
        
        return sign * result
