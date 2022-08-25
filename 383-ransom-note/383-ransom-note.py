class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word_set=set(ransomNote)
        
        for ch in word_set:
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        
        return True