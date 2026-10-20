class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        d={}
        n=len(numbers)
        for i in range(0,n):
            a=target-numbers[i]
            if a in d:
                return [d[a]+1,i+1]
            d[numbers[i]]=i
