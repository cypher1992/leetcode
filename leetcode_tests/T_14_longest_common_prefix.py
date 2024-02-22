import unittest
from typing import List

class Solution:
    """
        https://leetcode.com/problems/longest-common-prefix/description/
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        cpf = ""
        sortedStrs = sorted(strs)
        shortestStr = sortedStrs[0]
        longestStr = sortedStrs[-1]
        for char1, char2 in zip(shortestStr, longestStr):
            if char1 != char2:
                break
            cpf += char1
        return cpf


class SolutionTestCase(unittest.TestCase):
    case_1 = ["flower","flow","flight"]
    output1 = "fl"
    case_2 = ["dog","racecar","car"]
    output2 = ""
    function = Solution.longestCommonPrefix

    def test_case1(self):
        output = self.function(self.case_1,)
        self.assertEqual(self.output1, output)  

    def test_case2(self):
        output = self.function(self.case_2)
        print(output)
        self.assertEqual(self.output2, output)


    def test_zip(self):
        string = "Hello"
        string2 = "Hello2"
        for char1, char2 in zip(string,string2):
            print("String One Char", char1)
            print("String Two Char", char2)


    def test_zip2(self):
        string = ["HelloA1","HelloA2" ]
        string2 = ["HelloB1","HelloB2"]
        for list1_item,list2_item  in zip(string,string2):
            print("String Item ", list1_item)
            print("String2 Item", list2_item)

if __name__ == '__main__':
    unittest.main()
