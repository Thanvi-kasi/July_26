class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(start, target, path):
            if len(path) == k:
                if target == 0:
                    ans.append(path[:])
                return

            for i in range(start, 10):
                if i > target:
                    break
                path.append(i)
                backtrack(i + 1, target - i, path)
                path.pop()

        backtrack(1, n, [])
        return ans
