class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        INF = float('inf')

        dp = [[INF] * (op2 + 1) for _ in range(op1 + 1)]
        dp[0][0] = 0

        for x in nums:
            ndp = [[INF] * (op2 + 1) for _ in range(op1 + 1)]

            for a in range(op1 + 1):
                for b in range(op2 + 1):
                    if dp[a][b] == INF:
                        continue

                    ndp[a][b] = min(ndp[a][b], dp[a][b] + x)

                    if a < op1:
                        y = (x + 1) // 2
                        ndp[a + 1][b] = min(ndp[a + 1][b], dp[a][b] + y)

                    if b < op2 and x >= k:
                        ndp[a][b + 1] = min(ndp[a][b + 1], dp[a][b] + (x - k))

                    if a < op1 and b < op2:
                        best = INF

                        y = (x + 1) // 2
                        if y >= k:
                            best = min(best, y - k)

                        if x >= k:
                            z = (x - k + 1) // 2
                            best = min(best, z)

                        if best != INF:
                            ndp[a + 1][b + 1] = min(
                                ndp[a + 1][b + 1],
                                dp[a][b] + best
                            )

            dp = ndp

        return min(min(row) for row in dp)
