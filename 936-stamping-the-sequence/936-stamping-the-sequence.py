class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if stamp[0] != target[0] or stamp[-1] != target[-1]: return []
        n, m = len(stamp), len(target)
        path = [0] * m
        pos = collections.defaultdict(set)
        for i, c in enumerate(stamp): pos[c].add(i)

        def dfs(i, index):
            path[i] = index
            if i == m - 1: return index == n - 1
            nxt_index = set()
            if index == n - 1:  # rule 2
                nxt_index |= pos[target[i + 1]]
            elif stamp[index + 1] == target[i + 1]:  # rule 0
                nxt_index.add(index + 1)
            if stamp[0] == target[i + 1]:  # rule 1
                nxt_index.add(0)
            return any(dfs(i + 1, j) for j in nxt_index)

        def path2res(path):
            down, up = [], []
            for i in range(len(path)):
                if path[i] == 0:
                    up.append(i)
                elif i and path[i] - 1 != path[i - 1]:
                    down.append(i - path[i])
            return down[::-1] + up

        if not dfs(0, 0): return []
        return path2res(path)