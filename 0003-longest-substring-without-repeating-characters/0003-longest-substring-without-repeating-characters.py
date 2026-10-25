
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mx_length = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            length = right - left + 1
            if length > mx_length:
                mx_length = length

        return mx_length