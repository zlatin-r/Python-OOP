from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("TestTeam")

    def test_init(self):
        self.assertEqual(self.team.name, "TestTeam")
        self.assertEqual(self.team.members, {})


if __name__ == '__main__':
    main()
