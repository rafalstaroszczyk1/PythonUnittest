import unittest
from unittest.mock import patch
import employee_unittest


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = employee_unittest.Employee('Rafal', 'Staroszczyk', 200)
        self.emp_2 = employee_unittest.Employee('Jan', 'Kowalski', 100)

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Rafal.Staroszczyk@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jan.Kowalski@gmail.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Rafal Staroszczyk')
        self.assertEqual(self.emp_2.fullname, 'Jan Kowalski')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        print(self.emp_1.pay)
        self.assertEqual(self.emp_1.pay, 210)
        self.assertEqual(self.emp_2.pay, 105)

    def test_monthly_schedule(self):
        with patch('employee_unittest.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Staroszczyk/May')
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()