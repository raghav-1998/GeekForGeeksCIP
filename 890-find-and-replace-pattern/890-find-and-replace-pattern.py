class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
                return (word for word in words if (len(set(zip(word, pattern))) == len(set(pattern)) == len(set(word))))
