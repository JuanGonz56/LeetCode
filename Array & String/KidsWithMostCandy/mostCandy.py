class Solution:
   def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Step 1: Initialize the result list with False values for all kids
        result = [False for _ in range(len(candies))]

        # Step 2: Find the current maximum number of candies any kid has
        currentGreatestCandies = max(candies)

        # Step 3: Iterate through each kid's candies
        for i, currentCandies in enumerate(candies): 
            # Check if giving the extraCandies to the current kid
            # makes them have at least the same amount as the current max
            if currentCandies + extraCandies >= currentGreatestCandies:
                result[i] = True  # Mark as True since they can have the highest candies

        # Step 4: Return the boolean result list
        return result
