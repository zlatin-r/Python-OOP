from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("TestTeam")

    def test_init(self):
        self.assertEqual(self.team.name, "TestTeam")
        self.assertEqual(self.team.members, {})

    def test_name_setter_value_with_digit_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Na8me"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_remove_member_name_does_not_exist(self):
        res = self.team.remove_member("Peter")
        expect = "Member with name Peter does not exist"

        self.assertEqual(expect, res)


if __name__ == '__main__':
    main()
