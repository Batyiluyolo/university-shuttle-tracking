
# tests/test_abstract_factory.py

import unittest
from creational_patterns.abstract_factory import (
    DriverPackageFactory,
    StudentPackageFactory
)
from src.driver import Driver
from src.student import Student
from src.shuttle import Shuttle

class TestAbstractFactory(unittest.TestCase):
    def test_driver_package_factory(self):
        factory = DriverPackageFactory()
        user = factory.create_user()
        resource = factory.create_resource()

        self.assertIsInstance(user, Driver)
        self.assertIsInstance(resource, Shuttle)
        self.assertEqual(user.name, "James")
        self.assertEqual(resource.capacity, 30)

    def test_student_package_factory(self):
        factory = StudentPackageFactory()
        user = factory.create_user()
        resource = factory.create_resource()

        self.assertIsInstance(user, Student)
        self.assertIsInstance(resource, str)
        self.assertIn("Route View", resource)

if __name__ == "__main__":
    unittest.main()
