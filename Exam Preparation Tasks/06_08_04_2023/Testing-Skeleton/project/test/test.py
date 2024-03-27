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


if __name__ == '__main__':
    main()
