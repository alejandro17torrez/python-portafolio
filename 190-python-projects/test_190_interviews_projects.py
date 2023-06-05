import unittest

import numpy
from find_missing_numbers import find_missing_numbers
from group_anagrams import group_anagrams
from group_elements_of_same_index import group_elements_of_same_index


class Test190InterviewsProjects(unittest.TestCase):
    def test_find_missing_numbers(self):
        """
        Test if it gets missing numbers
        """

        input = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
        output_expected = [4, 12, 15]

        self.assertEqual(find_missing_numbers(input), output_expected)

    def test_group_anagrams(self):
        """
        Test group anagrams function
        """

        input = ["tea", "eat", "bat", "ate", "arc", "car"]
        output_expected = [["tea", "eat", "ate"], ["bat"], ["arc", "car"]]

        self.assertEqual(list(group_anagrams(input)), output_expected)

    def test_group_elements_of_same_index(self):
        """
        Test group elements of same index function
        """

        input = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        output_expected = numpy.array([[10, 40, 70], [20, 50, 80], [30, 60, 90]])

        self.assertEqual(
            group_elements_of_same_index(input).all(), output_expected.all()
        )


if __name__ == "__main__":
    unittest.main()
