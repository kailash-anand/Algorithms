class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = Counter(nums)
        print(table)
        vals = max(table.values())
        
        for x,y in table.items():
            if y == vals:
                return x