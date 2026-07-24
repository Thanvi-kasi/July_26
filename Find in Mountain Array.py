# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        ans = self.binary_search(mountainArr, target, 0, peak, True)
        if ans != -1:
            return ans

    
        return self.binary_search(mountainArr, target, peak + 1, n - 1, False)

    def binary_search(self, arr, target, left, right, ascending):
        while left <= right:
            mid = (left + right) // 2
            val = arr.get(mid)

            if val == target:
                return mid

            if ascending:
                if val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if val < target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
