class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group={}
        for i in strs:
            sortedword="".join(sorted(i))
            if sortedword not in group:
                group[sortedword]=[]
            group[sortedword].append(i)
        return list(group.values())
           
        