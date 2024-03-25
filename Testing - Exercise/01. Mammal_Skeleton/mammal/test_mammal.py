from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Simba", "Lion", "Roar")

    def test_correct_init(self):
        self.assertEqual("Simba", self.mammal.name)
        self.assertEqual("Lion", self.mammal.type)
        self.assertEqual("Roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_should_return_string(self):

        self.assertEqual("Simba makes Roar", self.mammal.make_sound())

    def test_info_should_return_string_whit_animal_name_and_type(self):

        self.assertEqual("Simba is of type Lion", self.mammal.info())


if __name__ == '__main__':
    main()
