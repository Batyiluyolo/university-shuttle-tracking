
# tests/test_simple_factory.py

import unittest
from creational_patterns.simple_factory import UserFactory
from src.student import Student
from src.driver import Driver
from src.user import User

class TestSimpleFactory(unittest.TestCase):
    def test_create_student(self):
        student = UserFactory.create_user(
            "student", "S001", "Luyolo", "luyolo@example.com", "password123",
            faculty="Engineering", year="3rd"
        )
        self.assertIsInstance(student, Student)
        self.assertEqual(student.faculty, "Engineering")

    def test_create_driver(self):
        driver = UserFactory.create_user(
            "driver", "D001", "Sam", "sam@example.com", "driverpass",
            license_number="ABC123456"
        )
        self.assertIsInstance(driver, Driver)
        self.assertEqual(driver.license_number, "ABC123456")

    def test_create_admin(self):
        admin = UserFactory.create_user(
            "admin", "A001", "Admin", "admin@example.com", "adminpass"
        )
        self.assertIsInstance(admin, User)
        self.assertEqual(admin.role, "Admin")

if __name__ == "__main__":
    unittest.main()
