import unittest

# Assuming you have a function 'calculate_roi' that takes a credit score and returns the ROI
def calculate_roi(credit_score):
	# Implementation of the credit scoring algorithm and ROI calculation
	# For demonstration purposes, let's use a simple linear relationship
	base_roi = 0.05
	roi_per_point = 0.01
	max_roi = 0.15

	roi = base_roi + roi_per_point * min(credit_score, 850)
	roi = min(roi, max_roi)

	return roi

class TestROICalculation(unittest.TestCase):

	def test_expected_roi_with_valid_credit_score(self):
		expected_roi = 0.12
		credit_score = 800
		roi = calculate_roi(credit_score)
		self.assertAlmostEqual(roi, expected_roi, places=2, msg="Unexpected ROI calculation")

	def test_roi_calculation_with_credit_score_below_minimum(self):
		credit_score = 300
		expected_roi = 0.05
		roi = calculate_roi(credit_score)
		self.assertAlmostEqual(roi, expected_roi, places=2, msg="Unexpected ROI for low credit score")

	def test_roi_calculation_with_credit_score_above_maximum(self):
		credit_score = 900
		expected_roi = 0.15
		roi = calculate_roi(credit_score)
		self.assertAlmostEqual(roi, expected_roi, places=2, msg="Unexpected ROI for high credit score")

	def test_roi_increases_linearly_with_credit_score(self):
		credit_score_1 = 600
		credit_score_2 = 700
		roi_1 = calculate_roi(credit_score_1)
		roi_2 = calculate_roi(credit_score_2)
		expected_roi_increase = 0.01 * (credit_score_2 - credit_score_1)
		self.assertAlmostEqual(roi_2 - roi_1, expected_roi_increase, places=2, msg="ROI increase not linear")

	def test_roi_is_capped_at_maximum_value(self):
		credit_score = 851  # Just above the cap
		expected_roi = 0.15
		roi = calculate_roi(credit_score)
		self.assertEqual(roi, expected_roi, msg="ROI not capped at maximum")

if __name__ == '__main__':
	unittest.main()
