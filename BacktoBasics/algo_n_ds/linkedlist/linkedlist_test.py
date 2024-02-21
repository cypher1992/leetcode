import unittest
from BacktoBasics.algo_n_ds.linkedlist.linkedlist import LinkedList

class MyTestCase(unittest.TestCase):

    def test_something(self):
        myll = LinkedList(4)
        self.assertEqual(myll.head.value, 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
