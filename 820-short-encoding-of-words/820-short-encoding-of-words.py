class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True)
        s=""
        
        for word in words:
            if(s.find(word+"#")==-1):
                s+=(word+"#")
        
        return len(s)