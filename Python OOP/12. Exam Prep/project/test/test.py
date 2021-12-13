from project.library import Library
import unittest


class TestLibrary(unittest.TestCase):

    def setUp(self) -> None:
        self.library = Library('name')

    def test_library__initialization(self):
        self.assertEqual('name', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_validation__with_white_space__raise_error(self):
        with self.assertRaises(Exception) as context:
            Library(' ')
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book__should_add_author_and_title(self):
        self.library.add_book('new_author', 'title')
        self.library.add_book('new_author', 'title1')

        self.assertEqual(2, len(self.library.books_by_authors['new_author']))

        self.library.add_book('new_author', 'title')

        self.assertEqual(2, len(self.library.books_by_authors['new_author']))
        self.assertTrue('new_author' in self.library.books_by_authors.keys())
        self.assertTrue(['title', 'title2'], self.library.books_by_authors['new_author'])


if __name__ == '__main__':
    unittest.main()
