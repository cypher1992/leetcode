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

    def test_set_index_1_to_4(self):
        myll = LinkedList(11)
        myll.append(3)
        myll.append(23)
        myll.append(7)
        myll.set_index(1,4)
        rs = myll.get(1)
        self.assertEqual(rs.value, 4)

    def test_insert_index_1_return_1(self):
        myll = LinkedList(0)
        myll.append(2)
        myll.insert(1,1)
        rs = myll.get(1)
        self.assertEqual(rs.value, 1)

    def test_insert_index_1_return_3(self):
        myll = LinkedList(0)
        myll.append(1)
        myll.append(2)
        myll.insert(3,3)
        rs = myll.get(3)
        self.assertEqual(rs.value, 3)

    def test_remove_23(self):
        myll = LinkedList(11)
        myll.append(3)
        myll.append(23)
        myll.append(7)
        rs = myll.remove(2)
        self.assertEqual(rs.value, 23)

    def test_reverse(self):
        myll = LinkedList(1)
        myll.append(2)
        myll.append(3)
        myll.append(4)
        myll.print_list()
        myll.reverse()
        myll.print_list()
        self.assertEqual(myll.get(0).next.value, 3)

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


    def test_replace(self):
        st00r ="()"
        def isValid(s: str) -> bool:
            stack = []
            special_chars = {')': '(', '}': '{', ']': '['}
            for c in s:
                if c in special_chars:
                    opposite_char = special_chars[c]
                    if len(stack) > 0 and stack[-1] == opposite_char:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)

            if len(stack) == 0:
                return True
            return False
        print(isValid(st00r))

    def test_string_reverse(self):
        string = str(121)
        reverseStr = string[::-1]
        print(reverseStr)

    def test_enumerate(self):
        x = [-1,-1,1,1,2,2,3,3,3,4,4,4,4,4,4]
        numset = sorted(set(x),reverse=True)
        count = len(numset)
        for i in range(len(x)):
            if numset:
                x[i] = numset.pop()
            else:
                x[i] = '_'
        print(x,count)

    def test_needle_in_haysack(self):
        needle = "sad"
        haystack = "1sadbutsad"
        location = haystack.find(needle)
        if location>-1:
            print(location)
        else:
            print(-1)

    def test_itertool(self):
        from itertools import permutations,combinations_with_replacement,product

        def count_ways_to_sum(numbers, target_sum):
            count = 0
            for r in range(1, target_sum + 1):
                for combination in product(numbers, repeat=r):
                    if sum(combination) == target_sum:
                        count += 1
            return count

        # Example usage:
        numbers = [1, 2]
        target_sum = 3
        ways_to_sum = count_ways_to_sum(numbers, target_sum)
        print("Number of ways to sum to", target_sum, ":", ways_to_sum)


    def test_climb_stairs(self):
        def climbStairs( n: int) -> int:
            if n == 0 or n == 1:
                return 1
            return climbStairs(n - 1) + climbStairs(n - 2)
        print(climbStairs(5))

    def test_bit(self):
        binary_string = "00111001011110000000000000000000"
        unsigned_integer = int(binary_string, 2)
        print(unsigned_integer)

    def test_number(self):
        num = bin(10000)
        print(type(num))
        print(num[:3])

    def test_find(self):
        x = [1,2,3]
        print(min(x))

    def test_index(self):
        nums1 = [0, 0, 0, 1, 2, 2, 3, 5, 6]
        nums1.sort()
        print(nums1)


        nums1[:] = [num for num in nums1 if num > 0]
        print(nums1)

    def test_2_sum(self):
        x = [1,2,3,3]
        target = 6
        for i in range(0,len(x)):
            for j in range(i,(len(x))):
                if x[i]+ x[j] == target:
                    print(x[i], x[j])
                    break
            x.pop(0)

    def test_2_sum_hashmap(self):
        x = [1, 2, 3, 3]
        target = 6
        hashmap = {v:i for i,v in enumerate(x)}
        print(hashmap)
        for i in range(len(x)):
            if hashmap.get(target-x[i]):
                print(x[i], x[hashmap[target-x[i]]])
                break


if __name__ == '__main__':
    unittest.main()
