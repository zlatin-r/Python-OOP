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


if __name__ == '__main__':
    main()
