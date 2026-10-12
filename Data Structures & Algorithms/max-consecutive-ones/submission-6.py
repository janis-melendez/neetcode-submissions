class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        amounts = []
        count = 0

        # track all consecutive counts
        for num in nums:
            if num == 0 and count > 0:
                amounts.append(count)
                count = 0
            elif num == 1:
                count += 1
        
        amounts.append(count)

        # return highest_amount
        return max(amounts)