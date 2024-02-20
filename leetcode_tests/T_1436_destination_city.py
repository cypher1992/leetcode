import unittest
from typing import List

class Solution:
    """
    https://leetcode.com/problems/destination-city/

    """
    def destCity(self, paths: List[List[str]]) -> str:
        start = {i[0] for i in paths}
        destination = {i[1] for i in paths}
        return list(destination - start)[0]



class MyTestCase(unittest.TestCase):
    case_1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    case_2 = [["B","C"],["D","B"],["C","A"]]
    case_3 = [["A","Z"]]
    function = Solution.destCity


    def test_case1(self):
        output = self.function(self.case_1)
        print(output)
        self.assertEqual("Sao Paulo", output)  # add assertion here

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
