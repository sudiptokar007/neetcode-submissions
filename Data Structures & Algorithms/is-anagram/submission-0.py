from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set()
        s_dict = defaultdict(int)
        t_set = set()
        t_dict = defaultdict(int)
        for i in s:
            s_set.add(i)
            s_dict[i]+=1
        for i in t:
            t_set.add(i)
            t_dict[i]+=1
        
        if len(s_set)!= len(t_set):
            return False
        for i in s_dict:
            if s_dict[i]!= t_dict[i]:
                return False
        return True
