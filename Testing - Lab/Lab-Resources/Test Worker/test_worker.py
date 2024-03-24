from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("Todor",
                             20_200,
                             200)

    def test_correct_init(self):
        self.assertEqual("Todor", self.worker.name)
        self.assertEqual(20_200, self.worker.salary)
        self.assertEqual(200, self.worker.energy)

    def test_work_when_worker_has_energy_expect_money_increase_and_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(self.worker.money, expected_money)
        self.assertEqual(self.worker.energy, expected_energy)

    def test_work_when_worker_does_not_have_energy_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest_increases_energy_whit_one(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()

        self.assertEqual(self.worker.energy, expected_energy)

    def test_get_info_returns_right_string(self):
        self.assertEqual('Todor has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
