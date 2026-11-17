import unittest

from src.fireai_assessment_codebase import (
    calculate_tax_new_regime,
    calculate_tax_old_regime,
    NYC311DataCorruptionInjector,
    NYC311DataQualityPipeline,
)


class IncludedSampleSmokeTests(unittest.TestCase):
    def setUp(self):
        self.profile = {
            "gross_salary": 1_500_000,
            "hra_received": 0,
            "rent_paid": 0,
            "basic_salary": 800_000,
            "city_type": "metro",
            "sec_80c": 150_000,
            "sec_80ccd_1b": 50_000,
            "sec_80d": 25_000,
            "home_loan_interest": 0,
        }

    def test_sample_tax_functions_return_nonnegative_numbers(self):
        old_tax = calculate_tax_old_regime(self.profile)
        new_tax = calculate_tax_new_regime(self.profile)
        self.assertIsInstance(old_tax, float)
        self.assertIsInstance(new_tax, float)
        self.assertGreaterEqual(old_tax, 0.0)
        self.assertGreaterEqual(new_tax, 0.0)

    def test_schema_check_accepts_required_fields(self):
        pipeline = NYC311DataQualityPipeline()
        record = {
            "unique_key": "1",
            "created_date": "2023-01-01 00:00:00",
            "agency": "ABC",
            "complaint_type": "Noise",
            "borough": "MANHATTAN",
        }
        self.assertTrue(pipeline.run_schema_checks(record))

    def test_schema_check_rejects_missing_required_field(self):
        pipeline = NYC311DataQualityPipeline()
        record = {"unique_key": "1", "created_date": "2023-01-01 00:00:00"}
        self.assertFalse(pipeline.run_schema_checks(record))

    def test_temporal_check_flags_closed_before_created(self):
        pipeline = NYC311DataQualityPipeline()
        record = {
            "created_date": "2023-01-01 00:00:00",
            "closed_date": "2022-01-01 00:00:00",
        }
        self.assertFalse(pipeline.run_temporal_checks(record))

    def test_latitude_longitude_injector_returns_swapped_copy(self):
        record = {"latitude": 40.7, "longitude": -73.9, "other": "kept"}
        result = NYC311DataCorruptionInjector.inject_swapped_lat_long(record)
        self.assertEqual(result["latitude"], -73.9)
        self.assertEqual(result["longitude"], 40.7)
        self.assertEqual(result["other"], "kept")
        self.assertEqual(record["latitude"], 40.7)

    def test_temporal_corruption_injector_creates_invalid_order(self):
        original = {
            "created_date": "2023-04-01 00:00:00",
            "closed_date": "2023-04-02 00:00:00",
        }
        corrupted = NYC311DataCorruptionInjector.inject_closed_before_created(original)
        pipeline = NYC311DataQualityPipeline()
        self.assertFalse(pipeline.run_temporal_checks(corrupted))
        self.assertEqual(original["created_date"], "2023-04-01 00:00:00")


if __name__ == "__main__":
    unittest.main()
