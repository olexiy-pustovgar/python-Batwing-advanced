import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("oliver", "stone", 25000)

    def test_email(self):
        self.assertEqual(self.employee.email, 'oliver.stone@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, 'oliver stone')

    def test_apply_raise(self):
        self.assertEqual(self.employee.pay*self.employee.raise_amt, 26250)

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mock_response):
        mock_response.return_value.text = "TEST"
        self.assertEqual(self.employee.monthly_schedule("june"), 'TEST')
