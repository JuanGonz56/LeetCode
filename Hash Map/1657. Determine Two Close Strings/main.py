class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Check if both strings have the same unique characters
        if set(word1) != set(word2):
            return False
        
        # Step 2: Count the frequency of each character in both strings
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # Step 3: Check if the sorted frequency lists match
        return sorted(freq1.values()) == sorted(freq2.values())