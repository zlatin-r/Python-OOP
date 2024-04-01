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

    def test_add_member(self):
        res = self.team.add_member(Ivan=35, Gosho=33)

        self.assertEqual(self.team.members, {"Ivan": 35, "Gosho": 33})
        self.assertEqual(res, "Successfully added: Ivan, Gosho")

    def test_remove_member_name_does_not_exist(self):
        res = self.team.remove_member("Peter")
        expect = "Member with name Peter does not exist"

        self.assertEqual(expect, res)

    def test_remove_member_happy_case(self):
        self.team.add_member(Todor=30)
        res = self.team.remove_member("Todor")
        expect = "Member Todor removed"

        self.assertEqual(expect, res)
        self.assertEqual(self.team.members, {})

    def test__gt__first_team_bigger(self):
        t1 = Team("TestTeam")
        t1.add_member(Pesho=20, Dian=34)
        t2 = Team("TestTeam")
        t2.add_member(Doncho=37)

        res = t1 > t2
        self.assertTrue(res, True)

    def test__gt__second_team_bigger(self):
        t1 = Team("TestTeam")
        t1.add_member(Pesho=20)
        t2 = Team("TestTeam")
        t2.add_member(Doncho=37, Dian=34)

        res = t1 > t2
        self.assertFalse(res, False)


if __name__ == '__main__':
    main()
