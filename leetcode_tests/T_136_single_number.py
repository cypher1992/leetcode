import unittest
from typing import List

class Solution:
    """
        https://leetcode.com/problems/single-number/description/
    """

    def singleNumberOriginal(self, nums: List[int]) -> int:
        numCounter = {}
        for i in nums:
            if numCounter.get(i):
                numCounter[i] = numCounter.get(i) + 1
            else:
                numCounter[i] = 1
        return list(dict(sorted(numCounter.items(), key=lambda x: x[1])).keys())[0]

    def singleNumber(self, nums: List[int]) -> int:
        temp = nums[0]
        for i in range(1, len(nums)):
            temp ^= nums[i]
        return temp


class SolutionTestCase(unittest.TestCase):
    case_1 = [2,2,1]
    output1 = 1
    case_2 = [4,1,2,1,2]
    output2 = 4
    case_3 = [1]
    output3 = 1
    function = Solution.singleNumber
    function2 = Solution.singleNumberOriginal

    def test_case1(self):
        output = self.function(self.case_1,)
        self.assertEqual(self.output1, output)  

    def test_case2(self):
        output = self.function(self.case_2)
        print(output)
        self.assertEqual(self.output2, output)

    def test_case3(self):
        output = self.function(self.case_3)
        print(output)
        self.assertEqual(self.output3, output)

    def test_case12(self):
        output = self.function2(self.case_1,)
        self.assertEqual(self.output1, output)

    def test_case23(self):
        output = self.function2(self.case_2)
        print(output)
        self.assertEqual(self.output2, output)

    def test_case34(self):
        output = self.function2(self.case_3)
        print(output)
        self.assertEqual(self.output3, output)
    
    def test_enumerate(self):
        """
        Enumerate associate position to the index location
        eg
        nums = range(1,9)
        for index,num in enumerate(1,9)
            print(index,num)

        0 , 1
        1, 2
        3, 4
        ....
        8,7
        """
        nums = range(1,9)
        for index, num in enumerate(nums):
            print(index,num)

    def test_xOr_operation(self):
        #print(1^1^2)
        #print(1 ^ 1 ^ 2)
        temp = 0
        for i in [1,1,1,2]:
            temp =temp^ i
            print(temp)
    
if __name__ == '__main__':
    unittest.main()
