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

    def test_add_new_win_sad_case_tournament_already_in_wins_return_string(self):
        self.tennis_player.wins = ["World Cup"]

        res = self.tennis_player.add_new_win("World Cup")
        expect = "World Cup has been already added to the list of wins!"

        self.assertEqual(expect, res)

    def test_add_new_win_happy_case_append_tournament_to_wins(self):
        self.tennis_player.add_new_win("World Cup")

        self.assertEqual(["World Cup"], self.tennis_player.wins)

    def test__lt__second_player_is_better(self):
        player = TennisPlayer("player", 30, 10)
        other = TennisPlayer("other", 30, 11)

        res = player < other

        self.assertEqual("other is a top seeded player and he/she is better than player", res)

    def test__lt__first_player_is_better(self):
        player = TennisPlayer("player", 30, 12)
        other = TennisPlayer("other", 30, 11)

        res = player < other

        self.assertEqual("player is a better player than other", res)

    def test__str__correct_string_message(self):
        self.tennis_player.wins = ["Win 1", "Win 2", "Win 3"]
        res = self.tennis_player.__str__()
        expected = f"Tennis Player: {self.tennis_player.name}\n" \
                   f"Age: {self.tennis_player.age}\n" \
                   f"Points: {self.tennis_player.points:.1f}\n" \
                   f"Tournaments won: {', '.join(self.tennis_player.wins)}"

        self.assertEqual(expected, res)


if __name__ == '__main__':
    main()
