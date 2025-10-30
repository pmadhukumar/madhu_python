class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()      # to store unique characters in current window
        left = 0              # left boundary of sliding window
        max_length = 0

        for right in range(len(s)):
            # If a duplicate is found, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character and update max length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
