class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = [False for _ in range(len(candies))]

        currentGreatestCandies = max(candies)

        for i, currentCandies in enumerate(candies): 
            if(currentCandies + extraCandies >= currentGreatestCandies):
                result[i] = True

        return result