import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 220)

    def test_vehicle_initialization(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(220, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive__when_needed_fuel_is_bigger__expect_exception(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(max_distance + 1)

        self.assertEqual('Not enough fuel', str(context.exception))

    def test_drive__when_needed_fuel_is_less__expect_reduce_fuel(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        self.vehicle.drive(max_distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel__when_fuel_is_greater_than_capacity__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1)

        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel__when_has_capacity_for_the_fuel__expect_add_to_fuel(self):
        distance = 10
        self.vehicle.drive(distance)
        recharge_fuel = (distance * self.vehicle.fuel_consumption) / 2
        expected_fuel = self.vehicle.fuel + recharge_fuel
        self.vehicle.refuel(recharge_fuel)

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_str_representation_result(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual = str(self.vehicle)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
