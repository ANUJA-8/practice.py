class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
    def maxEle(self):    
        for i in self.nums:
            print(count(self.nums)[i])
m=Solution([1,2,3,4,5,6,7,8,9,10])
print(m.maxEle())
        