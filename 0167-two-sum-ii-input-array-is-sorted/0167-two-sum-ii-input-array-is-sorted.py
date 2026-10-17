class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        d={}
        n=len(numbers)
        for i in range(n):
            a=target-numbers[i]
            if a in d:
                return [d[a]+1,i+1]
            else:
                d[numbers[i]]=i