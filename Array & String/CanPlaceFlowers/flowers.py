class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Add 0 at the beginning and end to avoid edge cases (handling boundary conditions)
        f = [0] + flowerbed + [0]

        # Iterate through the flowerbed (excluding the artificial boundaries)
        for i in range(1, len(f) - 1):  
            # Check if current spot and both adjacent spots are empty (0)
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1  # Plant a flower
                n -= 1    # Reduce the number of flowers needed

        # If we have planted at least `n` flowers, return True, otherwise False
        return n <= 0
