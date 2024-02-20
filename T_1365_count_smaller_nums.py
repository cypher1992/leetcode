import unittest
from typing import List

class Solution:
    """
    https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

    """
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter_lt = []
        for i in range(len(nums)):
            temp = nums.pop(0)
            count = 0
            for j in range(len(nums)):
                if temp > nums[j]:
                    count+=1
            counter_lt.append(count)
            nums.append(temp)
        return counter_lt



class MyTestCase(unittest.TestCase):
    case_1 = [8,1,2,2,3]
    case_2 = [["B","C"],["D","B"],["C","A"]]
    case_3 = [["A","Z"]]
    function = Solution.smallerNumbersThanCurrent


    def test_case1(self):
        output = self.function(self.case_1)
        self.assertEqual([4,0,1,1,3], output)  # add assertion here

    def test_case2(self):
        output = self.function(self.case_2)
        print(output)
        self.assertEqual("A", output)  # add assertion here

    def test_case3(self):
        output = self.function(self.case_3)
        print(output)
        self.assertEqual("Z", output)  # add assertion here

if __name__ == '__main__':
    unittest.main()
