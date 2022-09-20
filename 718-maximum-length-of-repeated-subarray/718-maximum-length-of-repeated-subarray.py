class Solution:  # 156 ms, faster than 98.97%
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        BASE, MOD = 101, 1_000_000_000_001
        hash1, hash2, POW = [0] * (m + 1), [0] * (n + 1), [1] * (max(m, n) + 1)
        for i in range(max(m, n)): POW[i + 1] = POW[i] * BASE % MOD  # Compute POW of BASE
        for i in range(m): hash1[i + 1] = (hash1[i] * BASE + nums1[i]) % MOD  # Compute hashing values of nums1
        for i in range(n): hash2[i + 1] = (hash2[i] * BASE + nums2[i]) % MOD  # Compute hashing values of nums2

        def getHash(h, left, right):  # 0-based indexing, right inclusive
            return (h[right + 1] - h[left] * POW[right - left + 1] % MOD + MOD) % MOD

        def foundSubArray(size):
            seen = defaultdict(list)
            for i in range(m - size + 1):
                h = getHash(hash1, i, i + size - 1)
                seen[h].append(i)
            for i in range(n - size + 1):
                h = getHash(hash2, i, i + size - 1)
                if h in seen:
                    for j in seen[h]:  # Double check - This rarely happens when collision occurs -> No change in time complexity
                        if nums1[j:j + size] == nums2[i:i + size]:
                            return True
            return False

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if foundSubArray(mid):
                ans = mid  # Update answer
                left = mid + 1  # Try to expand size
            else:
                right = mid - 1  # Try to shrink size
        return ans