import unittest

from magiclist import MagicList


class MagicListTest(unittest.TestCase):
    def test_new_elem(self):
        a = MagicList()
        a[0] = 5
        a[1] = 42
        a[2] = 121
        self.assertEqual(len(a), 3)
        self.assertEqual(a[0], 5)
        self.assertEqual(a[1], 42)
        self.assertEqual(a[2], 121)

    def test_index_error_insertion(self):
        a = MagicList()
        with self.assertRaises(IndexError):
            a[1] = 42

    def test_index_error_query(self):
        a = MagicList()
        with self.assertRaises(IndexError):
            b = a[1]


class MagicListClsTypeTest(unittest.TestCase):
    class Person:
        def __init__(self, age: int = None) -> None:
            self.age = age

    def test_new_elem(self):
        a = MagicList(cls_type=MagicListClsTypeTest.Person)
        a[0].age = 5
        self.assertEqual(len(a), 1)
        self.assertIsInstance(a[0], MagicListClsTypeTest.Person)
        self.assertEqual(a[0].age, 5)

    def test_index_error_insertion(self):
        a = MagicList()
        with self.assertRaises(IndexError):
            a[1].age = 42
