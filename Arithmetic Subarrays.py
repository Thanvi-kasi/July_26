class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []

        for left, right in zip(l, r):
            arr = sorted(nums[left:right + 1])
            diff = arr[1] - arr[0]
            ok = True

            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    ok = False
                    break

            ans.append(ok)

        return ans
