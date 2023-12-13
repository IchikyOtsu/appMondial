import unittest
from utils.classes.reservationManager import Reservation, ReservationManager


class TestReservationManager(unittest.TestCase):

    def setUp(self):
        self.manager = ReservationManager()
        self.res1 = Reservation("Nom1", "0123456789", 1, "2023-12-10 18:00", "eu", 0, 0, 1, 1)
        self.res2 = Reservation("Nom2", "9876543210", 2, "2023-12-11 19:00", "af", 0, 0, 2, 2)

    def test_addReservation(self):
        self.manager.addReservation(self.res1)
        self.assertIn(self.res1, self.manager.reservations)

    def test_findReservationById(self):
        self.manager.addReservation(self.res1)
        self.assertEqual(self.manager.findReservationById(1), self.res1)
        self.assertIsNone(self.manager.findReservationById(999))

    def test_removeReservation(self):
        self.manager.addReservation(self.res1)
        self.manager.removeReservation(self.res1)
        self.assertNotIn(self.res1, self.manager.reservations)

    def test_findReservationByName(self):
        self.manager.addReservation(self.res1)
        self.assertEqual(self.manager.findReservationByName("Nom1"), self.res1)
        self.assertIsNone(self.manager.findReservationByName("Inexistant"))

    def test_findReservationByTable(self):
        self.manager.addReservation(self.res1)
        self.manager.addReservation(self.res2)
        self.assertEqual(self.manager.findReservationByTable(1), [self.res1])
        self.assertEqual(self.manager.findReservationByTable(3), [])

    def test_to_json(self):
        self.manager.addReservation(self.res1)
        self.manager.addReservation(self.res2)
        expected_output = {
            "reservations": [self.res1.to_json(), self.res2.to_json()]
        }
        self.assertEqual(self.manager.to_json(), expected_output)

    def test_from_json(self):
        data = {
            "reservations": [self.res1.to_json(), self.res2.to_json()]
        }
        manager_from_json = ReservationManager.from_json(data)
        self.assertEqual(len(manager_from_json.reservations), 2)
        self.assertEqual(manager_from_json.reservations[0].nom, "Nom1")
        self.assertEqual(manager_from_json.reservations[1].nom, "Nom2")

if __name__ == '__main__':
    unittest.main()
