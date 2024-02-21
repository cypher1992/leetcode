import unittest
from typing import List

class Solution:
    """
        Say you have a bag of items with current weight(cw)
        you have list of items(i) with each weight
        you need to find max number items you can put into bag based on location
    """

    def findOptimalWeight(self, maxcap:int,cw:int, items: List[int]) -> List[int]:
        res = []
        loc = {item: index for index,item in enumerate(items)}
        remainder = maxcap-cw
        sortedx = sorted(items.copy())
        for i in sortedx:
            if remainder-i > 0:
                res.append(i)
                remainder-=i
        return [loc.get(i) for i in items if i in res and loc.get(i) is not None]


class SolutionTestCase(unittest.TestCase):
    case_1 = [25,2,3,7,50,60,100]
    case_1_cw = 450
    case_1_mw = 500
    output1 = [0,1,2,3]
    case_2 = [7,52,45]
    case_2_cw = 490
    case_2_mw = 500
    output2 = [0]
    case_3 = [2,3,7]
    case_3_cw = 499
    case_3_mw = 500
    output3 = []
    function = Solution.findOptimalWeight

    def test_case1(self):
        output = self.function(self.case_1_mw,self.case_1_cw,self.case_1)
        self.assertEqual(self.output1, output)  



    
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
    
if __name__ == '__main__':
    unittest.main()
