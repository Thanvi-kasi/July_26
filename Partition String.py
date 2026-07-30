class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        curr = ""

        for ch in s:
            curr += ch
            if curr not in seen:
                seen.add(curr)
                res.append(curr)
                curr = ""

        return res
