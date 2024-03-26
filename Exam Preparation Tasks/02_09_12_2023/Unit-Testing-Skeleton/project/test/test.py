from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Aytos")

    def test_init(self):
        self.assertEqual("Aytos", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_with_len_less_than_three_raises_value_error(self):
        expected_message = "Name should be more than 3 symbols!"

        with self.assertRaises(ValueError) as ve:
            self.station.name = "NY"

        self.assertEqual(expected_message, str(ve.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("train1")
        self.assertEqual(deque(["train1"]), self.station.arrival_trains)

    def test_train_has_arrived__expect_other_trains(self):
        self.station.new_arrival_on_board("train1")
        self.station.new_arrival_on_board("train2")

        expect = "There are other trains to arrive before Test Train3."
        actual = self.station.train_has_arrived('Test Train3')
        self.assertEqual(expect, actual)

    def test_train_has_arrived__expect_proper_train_departure_no_initial_trains(self):
        self.station.new_arrival_on_board("Test Train")
        expect = "Test Train is on the platform and will leave in 5 minutes."
        actual = self.station.train_has_arrived('Test Train')
        self.assertEqual(expect, actual)

    def test_train_has_arrived__expect_proper_train_departure(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train2")
        expect = "Test Train is on the platform and will leave in 5 minutes."
        actual = self.station.train_has_arrived('Test Train')
        self.assertEqual(expect, actual)

    def test_train_has_arrived__expect_proper_train_arrive_pop(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train2")
        self.station.train_has_arrived("Test Train")
        expect = deque(["Test Train2"])
        actual = self.station.arrival_trains
        self.assertEqual(expect, actual)

    def test_train_has_left_empty_station__expect_false(self):
        self.station.new_arrival_on_board("")
        self.station.train_has_arrived("")

        actual = self.station.train_has_left("Test Train")

        self.assertFalse(actual)

    def test_train_has_left__expect_false(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train2")
        self.station.train_has_arrived("Test Train")
        self.station.train_has_arrived("Test Train2")

        actual = self.station.train_has_left("Test Train2")
        self.assertFalse(actual)

    def test_train_has_left__expect_true(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.train_has_arrived("Test Train")

        actual = self.station.train_has_left("Test Train")
        self.assertTrue(actual)



if __name__ == '__main__':
    main()
