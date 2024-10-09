class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = defaultdict(int)   # Step 1: Initialize a defaultdict with int (which defaults to 0).
        
        for item in arr:   # Step 2: Loop over the array and count occurrences of each item.
            count_dict[item] += 1
        
        items = set()   # Step 3: Initialize a set to store unique frequencies of occurrences.
        
        for freq in count_dict.values():   # Step 4: Loop over the frequencies (values of the dictionary).
            if freq in items:   # Step 5: If the frequency already exists in the set, return False.
                return False
            else:
                items.add(freq)   # Step 6: Otherwise, add the frequency to the set.
            
        return True   # Step 7: If all frequencies are unique, return True.
