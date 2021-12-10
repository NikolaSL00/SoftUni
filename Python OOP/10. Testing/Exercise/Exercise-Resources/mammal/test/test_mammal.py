from project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('name', 'mammal_type', 'sound')

    def test_initialization__with_valid_values__expect_valid_initialization(self):
        name = 'Name'
        m_type = 'Type'
        sound = 'Sound'
        mammal = Mammal(name, m_type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(m_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound__expect_valid_string(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        actual = self.mammal.make_sound()

        self.assertEqual(expected, actual)

    def test_get_kingdom__expect_valid_kingdom(self):
        expected = 'animals'
        actual = self.mammal.get_kingdom()

        self.assertEqual(expected, actual)

    def test_info__expect_valid_string_representation(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        actual = self.mammal.info()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
