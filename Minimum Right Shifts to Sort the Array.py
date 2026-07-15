class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        drops = 0
        drop_index = -1

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
                drop_index = i

        if drops == 0:
            return 0
        if drops > 1:
            return -1

        return n - (drop_index + 1)
