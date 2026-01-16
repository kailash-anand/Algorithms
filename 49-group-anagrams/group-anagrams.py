from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for x in strs:
            key = tuple(sorted(x))    
            result[key].append(x)

        return list(result.values())




                
            

            