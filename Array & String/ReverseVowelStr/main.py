class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        strVowel = []
        placeVal = []

        for i in range(len(s)):
            if s[i] in vowels:  # Check if the character is a vowel
                strVowel.append(s[i])
                placeVal.append(i)  # Append the index of the vowel
        
        strVowel.reverse()

        # Construct the result string by replacing vowels with reversed vowels
        result = list(s)
        for j in range(len(placeVal)):
            result[placeVal[j]] = strVowel[j]

        return ''.join(result)