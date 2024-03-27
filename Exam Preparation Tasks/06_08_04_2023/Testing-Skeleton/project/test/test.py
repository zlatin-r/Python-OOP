from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.tennis_player = TennisPlayer("Ivan", 30, 10.0)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.tennis_player.name)
        self.assertEqual(30, self.tennis_player.age)
        self.assertEqual(10.0, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_setter_name_with_len_two_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "Jo"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_setter_age_value_less_than_18_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))


if __name__ == '__main__':
    main()
