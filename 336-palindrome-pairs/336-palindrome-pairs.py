class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wmap, ans = {}, []
        for i in range(len(words)):
            wmap[words[i]] = i
        for i in range(len(words)):
            if words[i] == "":
                for j in range(len(words)):
                    w = words[j]
                    if self.isPal(w, 0, len(w)-1) and j != i:
                        ans.append([i, j])
                        ans.append([j, i])
                continue
            bw = words[i][::-1]
            if bw in wmap:
                res = wmap[bw]
                if res != i: ans.append([i, res])
            for j in range(1, len(bw)):
                if bw[j:] in wmap and self.isPal(bw, 0, j - 1):
                    ans.append([i, wmap[bw[j:]]])
                if bw[:j] in wmap and self.isPal(bw, j, len(bw)-1):
                    ans.append([wmap[bw[:j]], i])
        return ans

    def isPal(self, word: str, i: int, j: int) -> bool:
        while i < j:
            if word[i] != word[j]: return False
            i += 1
            j -= 1
        return True
