import unittest
from BacktoBasics.algo_n_ds.linkedlist.linkedlist import LinkedList

class MyTestCase(unittest.TestCase):

    def test_head_is_None(self):
        myll = LinkedList()
        self.assertEqual(myll.head.value, None)

    def test_tail_is_None(self):
        myll = LinkedList()
        self.assertEqual(myll.tail.value, None)

    def test_length_is_None(self):
        myll = LinkedList()
        self.assertEqual(myll.length, 1)

    def test_head(self):
        myll = LinkedList(4)
        self.assertEqual(myll.head.value, 4)  # add assertion here

    def test_tail(self):
        myll = LinkedList(4)
        self.assertEqual(myll.tail.value, 4)

    def test_length(self):
        myll = LinkedList(4)
        self.assertEqual(myll.length, 1)

    def test_append(self):
        myll = LinkedList(1)
        myll.append(2)
        myll.print_list()

if __name__ == '__main__':
    unittest.main()
