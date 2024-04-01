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

    def test_name_happy_case(self):
        self.team.name = "TeamOne"

        self.assertEqual("TeamOne", self.team.name)

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

    def test__len__(self):
        self.team.add_member(Kolyo=39, Dancho=31)

        self.assertEqual(len(self.team), 2)

    def test__add__(self):
        t1 = Team("FirstTeam")
        t1.add_member(Stefan=35)
        t2 = Team("SecondTeam")
        t2.add_member(Niki=31)
        new_team = t1 + t2
        new_team.add_member(Pesho=21, Todor=22)

        self.assertEqual(new_team.name, "FirstTeamSecondTeam")
        self.assertEqual(new_team.members, {'Niki': 31, 'Pesho': 21, 'Stefan': 35, 'Todor': 22})

    def test__str__(self):
        self.team.add_member(Gosho=21, Tosho=31)
        res = self.team.__str__()
        expect = "Team name: TestTeam\nMember: Tosho - 31-years old\nMember: Gosho - 21-years old"

        self.assertEqual(res, expect)


if __name__ == '__main__':
    main()
