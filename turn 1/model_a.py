import unittest


def calculate_roi(credit_score, loan_amount, interest_rate):
    # Simple credit scoring algorithm for demonstration
    base_rate = 0.05
    if credit_score >= 700:
        interest_rate = base_rate - 0.02
    elif credit_score >= 600:
        interest_rate = base_rate - 0.01

    roi = (interest_rate * loan_amount) / loan_amount * 100
    return roi


class TestROICalculation(unittest.TestCase):

    def test_anticipated_roi(self):
        """
        Semantic test case to verify the anticipated ROI for a given credit score scenario.
        """
        credit_score = 750
        loan_amount = 10000
        expected_roi = 1.8  # Anticipated ROI based on the credit scoring logic

        calculated_roi = calculate_roi(credit_score, loan_amount, 0)

        # Assertion to check if the calculated ROI matches the expected ROI
        self.assertAlmostEqual(calculated_roi, expected_roi, places=2, msg="ROI calculation failed")


if __name__ == '__main__':
    unittest.main()
