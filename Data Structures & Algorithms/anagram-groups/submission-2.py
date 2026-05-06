from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for s in strs:
            st="".join(sorted(s))
            seen[st].append(s)
        print(seen.values())
        return list(seen.values())




