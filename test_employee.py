"""
Employee class test.
"""

import unittest
from employee import Employee

NAME: str = 'Rodrigo'
EMPLOYEE_ID: int = 722

class TestEmployeeComputePayout(unittest.TestCase):
    """Test the compute_payout method of the Employee class"""

    def setUp(self):
        """Set up test fixtures"""
        self.rodrigo = Employee(name=NAME,employee_id=EMPLOYEE_ID)

    def test_employee_payout_returns_a_float(self):
        """Wheter payout returns a float"""
        self.assertIsInstance(self.rodrigo.compute_payout(), float)

    def test_employee_payout_no_commission_no_hours(self):
        """Wheter payout is correctly computed in caso of no comission and no hours worked"""
        self.assertAlmostEqual(self.rodrigo.compute_payout(), 1000.0)

    def test_employee_payout_no_comission(self):
        """Wheter payout is correctly computed in caso of no comission"""
        self.rodrigo.hours_worked = 10.0
        self.assertAlmostEqual(self.rodrigo.compute_payout(), 2000.0)

    def test_employee_payout_with_comission(self):
        """Wheter payout is correctly computed in case of 10 contracts landed and 10 hours worked"""

        self.rodrigo.hours_worked = 10.0
        self.rodrigo.contracts_landed = 10
        self.assertAlmostEqual(self.rodrigo.compute_payout(), 3000.0)        

    def test_employee_payout_with_comission_disabled(self):
        """Wheter payout is correctly computed in case of 10 contracts landed and 10 hours worked
        but commission is disabled"""

        self.rodrigo.hours_worked = 10.0
        self.rodrigo.contracts_landed = 10
        self.rodrigo.has_commission = False
        self.assertAlmostEqual(self.rodrigo.compute_payout(), 2000.0)


if __name__ == '__main__':
    unittest.main()