
class Solution:
    def trap(self, height: List[int]) -> int:
        left_m = float("-inf")
        right_m = float("-inf")
        
        total_trap_water = 0
        left_max_array = []
        right_max_array = []

        for i in range(len(height)):
            if left_m < height[i]:
                left_m = height[i]
            left_max_array.append(left_m)

        for i in range(len(height) - 1, -1, -1):
            if right_m < height[i]:
                right_m = height[i]
            right_max_array.append(right_m)

        right_max_array.reverse()

        for i in range(1, len(height) - 1):
            total_trap_water += (
                min(left_max_array[i], right_max_array[i]) - height[i]
            )

        return total_trap_water

