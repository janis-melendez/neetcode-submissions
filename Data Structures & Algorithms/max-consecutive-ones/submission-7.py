def return_max(num1, num2):
    return max(num1, num2)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0

        for num in nums:
            if num == 0:
                max_count = return_max(count, max_count)
                count = 0
            elif num == 1:
                count += 1
        
        max_count = return_max(count, max_count)

        return max_count