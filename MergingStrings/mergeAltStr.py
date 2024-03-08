class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        mergStr = ''
        while i < len(word1) and j < len(word2):
            mergStr += word1[i]
            mergStr += word2[j]
            i += 1
            j += 1
        
        while i < len(word1):
            mergStr += word1[i]
            i += 1

        while j < len(word2):
            mergStr += word2[j]
            j += 1
            
        return mergStr
    
