class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        even = 1  
        odd = 0
        prefix = 0
        ans = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                ans = (ans + odd) % MOD
                even += 1
            else:
                ans = (ans + even) % MOD
                odd += 1

        return ans
