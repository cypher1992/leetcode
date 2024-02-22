import unittest


class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        https://leetcode.com/problems/reverse-string/
        """
        return [s[i-1] for i in range(len(s), 0,-1)]


class MyTestCase(unittest.TestCase):

    def test_case1(self):
        output = Solution().reverseString(["h","e","l","l","o"])
        self.assertEqual(["o","l","l","e","h"], output)  # add assertion here


    def test_case2(self):
        output = Solution().reverseString(["H","a","n","n","a","h"])
        self.assertEqual(["h","a","n","n","a","H"], output)  # add assertion here

    def test_length_min(self):
        strs = ["flower", "flow", "flight"]
        sortedStrs = sorted(strs)
        print(sortedStrs)

if __name__ == '__main__':
    unittest.main()
