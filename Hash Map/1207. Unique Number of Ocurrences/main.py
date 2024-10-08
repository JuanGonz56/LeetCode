class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = defaultdict(int)

        for item in arr:
            count_dict[item] += 1
        
        items = set()

        for freq in count_dict.values():
            if freq in items:
                return False
            else:
                items.add(freq)
        
        return True
