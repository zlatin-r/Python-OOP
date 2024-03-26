from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestProject(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot(
            "Mountain",
            "Arm",
            100,
            200)

    def test_correct_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Arm", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_with_not_allowed_value_raises_exception(self):
        expected_message = f"Category should be one of {self.ALLOWED_CATEGORIES}"
        with self.assertRaises(Exception) as ex:
            self.robot.category = "Not allowed"

        self.assertEqual(expected_message, str(ex.exception))

    def test_get_used_capacity(self):
        software1 = {"name": "Software1", "capacity_consumption": 30, "memory_consumption": 50}
        software2 = {"name": "Software2", "capacity_consumption": 40, "memory_consumption": 70}
        self.robot.installed_software = [software1, software2]
        self.assertEqual(self.robot.get_used_capacity(), 70)

    def test_get_available_capacity(self):
        self.robot.installed_software = [{'capacity_consumption': 30}]
        self.assertEqual(self.robot.get_available_capacity(), 70)

    def test_get_used_memory(self):
        software1 = {"name": "Software1", "capacity_consumption": 30, "memory_consumption": 50}
        software2 = {"name": "Software2", "capacity_consumption": 40, "memory_consumption": 70}
        self.robot.installed_software = [software1, software2]
        self.assertEqual(self.robot.get_used_memory(), 120)

    def test_get_available_memory(self):
        self.robot.installed_software = [{'memory_consumption': 30}]
        self.assertEqual(self.robot.get_available_memory(), 170)

    def test_install_software_success(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}

        result = self.robot.install_software(software)
        self.assertEqual(result, f"Software '{software['name']}' successfully installed on {self.robot.category} part.")
        self.assertEqual(self.robot.installed_software, [software])

    def test_install_software_exact_capacity_memory(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}

        self.robot.capacity = software['capacity_consumption']
        self.robot.memory = software['memory_consumption']

        result = self.robot.install_software(software)

        expected_message = f"Software '{software['name']}' successfully installed on {self.robot.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.robot.installed_software, [software])

    def test_install_software_memory_condition_only(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}

        self.robot.capacity = software['capacity_consumption'] - 5
        self.robot.memory = software['memory_consumption'] + 10

        result = self.robot.install_software(software)


        expected_message = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_capacity_condition_only(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}

        self.robot.capacity = software['capacity_consumption'] + 10
        self.robot.memory = software['memory_consumption'] - 5

        result = self.robot.install_software(software)

        expected_message = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_failure(self):
        software = {'name': 'Software1', 'capacity_consumption': 150, 'memory_consumption': 250}

        result = self.robot.install_software(software)

        expected_message = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.robot.installed_software, [])


if __name__ == '__main__':
    main()
