from typing import List
from collections import defaultdict

class Solution: 
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Initialize a dictionary to store the count of each unique row in the grid.
        row_count = defaultdict(int)

        # Initialize a counter for pairs of equal rows and columns.
        count = 0

        # Iterate over each row in the grid.
        # Convert each row to a tuple (so it can be used as a dictionary key) and
        # increment its count in the row_count dictionary.
        for row in grid:
            row_count[tuple(row)] += 1

        # Use the zip function with unpacking (*) on the grid to iterate over columns.
        # zip(*grid) effectively transposes the grid, turning columns into rows.
        for column in zip(*grid):
            # Check if this "column as a row" matches any of the rows we've counted.
            # If it does, add the count of matching rows to the total count.
            count += row_count[column]

        # Return the total count of equal row-column pairs.
        return count
