class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}

        left, counter, res = 0, 0, 0

        for right in range(len(s)):
            counter += 1 if s[right] in vowel else 0
            if right - left + 1 > k:
                counter -= 1 if s[left] in vowel else 0
                left += 1

            res = max(res, counter)

        return res