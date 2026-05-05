from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp=defaultdict(list)
        #key is word value is list 

        for word in strs:
            key=''.join(sorted(word)) #sorted returns list ''.join is use to conver back to string
            mp[key].append(word)
        return list(mp.values()) #extracts the list from mp

