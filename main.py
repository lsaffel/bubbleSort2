class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort

        secondLast = len(nums) - 1
        while secondLast >= 1:
            for i in range(secondLast):
                j = i + 1
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
            secondLast -= 1

        return nums
