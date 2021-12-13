from unittest import TestCase, main

from custom_list import CustomList


class CustomListTest(TestCase):

    def setUp(self) -> None:
        self.cl = CustomList()

    def test_append_should_add_element(self):
        result = self.cl.append(1)

        self.assertEqual(1, result[0])
        self.assertEqual(1, len(self.cl))
        self.assertEqual(1, self.cl.get(0))

    def test_append_should_add_element_to_the_end(self):
        self.cl.append(1)
        result = self.cl.append(2)

        self.assertEqual([1, 2], result)
        self.assertEqual(2, len(self.cl))
        self.assertEqual(2, self.cl.get(1))

    def test_remove_should_with_no_integer_raise(self):
        with self.assertRaises(IndexError) as context:
            self.cl.remove('st')

        self.assertEqual('st is not an integer.', str(context.exception))

    def test_remove_with_invalid_raises(self):
        indices = [-1, 100, -5]

        for idx in indices:
            with self.assertRaises(IndexError) as context:
                self.cl.remove(idx)
            self.assertEqual(f'{idx} is invalid index', str(context.exception))

    def test_remove_with_valid_index_should_remove_the_element(self):
        n = 5
        for num in range(n):
            self.cl.append(num)
        self.assertEqual(0, self.cl.remove(0))
        self.assertNotIn(0, self.cl)
        self.assertEqual(n - 1, self.cl.remove(len(self.cl) - 1))
        self.assertNotIn(n - 1, self.cl)

        self.assertEqual(n - 2, len(self.cl))

    def test_get_with_invalid_index(self):
        indices = ['str', 1.5, [], {}, (1, 2, 3), -1, 100]

        for idx in indices:
            with self.assertRaises(Exception):
                self.cl.get(idx)

    def test_get_should_return_the_element_on_index(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)

        self.assertEqual(1, self.cl.get(0))
        self.assertEqual(2, self.cl.get(1))
        self.assertEqual(3, self.cl.get(2))

    def test_extend_should_add_iterable_to_initial_list(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)

        iterable = [4, 5]

        result = self.cl.extend(iterable)
        self.assertEqual([1, 2, 3, 4, 5], result)
        self.assertNotEqual(id(result), id(self.cl._CustomList__elements))




if __name__ == '__main__':
    main()
