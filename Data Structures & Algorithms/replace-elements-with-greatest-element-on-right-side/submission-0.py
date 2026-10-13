class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        answer = [0] * n
        rightMax = -1
        for i in range (n - 1, -1, -1):
            answer[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return answer