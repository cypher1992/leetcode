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

    def test_pop(self):
        myll = LinkedList(1)
        myll.append(2)
        print(myll.pop())
        print(myll.pop())
        print(myll.pop())

    def test_prepend(self):
        myll = LinkedList(2)
        myll.append(3)
        myll.prepend(1)
        self.assertTrue(myll.head.value == 1 and myll.length ==3)

    def test_pop_first_3items(self):
        myll = LinkedList(3)
        myll.append(2)
        myll.append(1)
        for i in range(myll.length+1):
            rs =myll.pop_first()
            if rs:
                print(rs.value)
            else:
                print(rs)
        self.assertIsNone(rs)

    def test_get_index_node(self):
        myll = LinkedList(3)
        myll.append(2)
        myll.append(1)
        rs = myll.get(2)
        self.assertEqual(rs.value,1)
    #####

    def test_something(self):
        def word_to_number(word):
            word = word.lower()
            word_dict = {
                "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
                "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
                "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
                "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30",
                "forty": "40", "fifty": "50", "sixty": "60", "seventy": "70",
                "eighty": "80", "ninety": "90", "hundred": "100", "thousand": "1000",
                "million": "1000000", "billion": "1000000000"
            }

            if word in word_dict:
                return word_dict[word]

            # Handle composite numbers like "twenty-one", "thirty-two", etc.
            if '-' in word:
                prefix, suffix = word.split('-')
                return str(int(word_dict[prefix]) + int(word_dict[suffix]))

            return "Not a recognized number word"

        def text_to_number(text):
            words = text.split()
            numeric_words = []
            for word in words:
                if word.lower() == 'and':
                    continue
                numeric_word = word_to_number(word)
                if numeric_word != "Not a recognized number word":
                    numeric_words.append(numeric_word)
            return str(sum(map(int, numeric_words)))


        print(text_to_number("one billion two hundred thirty eight million"))

if __name__ == '__main__':
    unittest.main()
