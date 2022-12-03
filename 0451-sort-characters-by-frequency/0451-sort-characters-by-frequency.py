class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        arr = [[freq, c] for c, freq in cnt.items()]
        arr.sort(key=lambda x:-x[0])  # sort in decreasing order by frequency
        ans = []
        for freq, c in arr:
            ans.append(freq * c)
        return "".join(ans)