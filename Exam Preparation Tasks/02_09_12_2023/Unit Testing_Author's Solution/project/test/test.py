from unittest import TestCase, main
from collections import deque
from project.railway_station import RailwayStation


class TestRailwayStationClass(TestCase):
    name = 'Test Station'
    arrival_trains = []
    departure_trains = []

    def setUp(self):
        self.station = RailwayStation(name="Test Station")

    def test_railway_station_structure(self):
        self.assertTrue(hasattr(RailwayStation, "new_arrival_on_board"))
        self.assertTrue(hasattr(RailwayStation, "train_has_arrived"))
        self.assertTrue(hasattr(RailwayStation, "train_has_left"))

        self.assertTrue(isinstance(getattr(RailwayStation, "name"), property))

    def test_init(self):
        self.assertEqual('Test Station', self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_with_only_2_symbols__expect_to_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.station = RailwayStation(name="Te")

        expect = "Name should be more than 3 symbols!"
        actual = str(ve.exception)
        self.assertEqual(expect, actual)

    def test_name_with_exactly_3_symbols__expect_to_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.station = RailwayStation(name="Tes")

        expect = "Name should be more than 3 symbols!"
        actual = str(ve.exception)
        self.assertEqual(expect, actual)

    def test_name__expect_to_success(self):
        self.station.name = "Test"
        expect = "Test"
        actual = self.station.name
        self.assertEqual(expect, actual)

    def test_new_arrival_on_board_success(self):
        self.station.new_arrival_on_board("Test Train")
        self.assertEqual(self.station.arrival_trains, deque(["Test Train"]))

    def test_train_has_arrived__expect_other_trains(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train2")
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