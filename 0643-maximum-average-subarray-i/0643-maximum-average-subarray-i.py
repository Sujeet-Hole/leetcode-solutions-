
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = 0
        left = 0

        for i in range(k):
            total += nums[i]

        max_average = total / k

        for i in range(k, len(nums)):
            total -= nums[left]
            total += nums[i]
            left += 1

            current_average = total / k

            if current_average > max_average:
                max_average = current_average

        return max_average

