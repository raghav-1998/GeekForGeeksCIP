class Solution:
    def breakPalindrome(self, S):
        n=len(S)
        for i in range(n// 2):
            if S[i] != 'a':
                return S[:i] + 'a' + S[i + 1:]
        return S[:-1] + 'b' if S[:-1] else ''