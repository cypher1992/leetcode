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

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        counter_lt = []
        counter_dict = {}
        numbers = sorted(nums.copy())
        for i in range(len(numbers)):
            if numbers[i] == numbers[i-1] and i>0:
                counter_lt.append(counter_lt[len(counter_lt)-1])
            else:
                counter_lt.append(len(numbers[:i]))
            counter_dict[numbers[i]] = counter_lt[len(counter_lt)-1]
        return [counter_dict.get(i) for i in nums]


class MyTestCase(unittest.TestCase):
    case_1 = [8,1,2,2,3]
    output1 = [4,0,1,1,3]
    case_2 = [6,5,4,8]
    output2 = [2,1,0,3]
    case_3 = [7,7,7,7]
    output3 = [0,0,0,0]
    function = Solution.smallerNumbersThanCurrent
    function2 = Solution.smallerNumbersThanCurrent2


    def test_case1(self):
        output = self.function(self.case_1)
        self.assertEqual(self.output1, output)  # add assertion here

    def test_case2(self):
        output = self.function(self.case_2)
        print(output)
        self.assertEqual(self.output2, output)  # add assertion here

    def test_case3(self):
        output = self.function(self.case_3)
        print(output)
        self.assertEqual(self.output3, output)  # add assertion here

    def test_case4(self):
        output = self.function2(self.case_1)
        self.assertEqual(self.output1, output)  # add assertion here

if __name__ == '__main__':
    unittest.main()
