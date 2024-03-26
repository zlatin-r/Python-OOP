from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestProject(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot(
            "Mountain",
            "some_part",
            10,
            20)

    def test_correct_input(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("some_part", self.robot.part_type)
        self.assertEqual(10, self.robot.capacity)
        self.assertEqual(20, self.robot.memory)




if __name__ == '__main__':
    main()
