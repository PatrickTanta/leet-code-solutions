
class Solution:
    def runningSum(self, nums):
        return [sum(nums[:i]) for i in range(1, len(nums)+1)]

solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))
