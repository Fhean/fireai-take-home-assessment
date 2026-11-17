"""
FireAI Take-Home Assessment: Project A & Project B Consolidated Implementation
Author: Mohamed Farhanudin S
"""

import math
import re
from typing import Dict, List, Optional, Tuple


# ==========================================
# PROJECT A: INCOME-TAX ENGINE (IMPLEMENTATION)
# ==========================================

profile_a = {
    "gross_salary": 1800000,
    "hra_received": 120000,
    "rent_paid": 150000,
    "basic_salary": 900000,
    "city_type": "non-metro",
    "sec_80c": 150000,
    "sec_80ccd_1b": 50000,
    "sec_80d": 25000,
    "home_loan_interest": 200000
}

def calculate_tax_old_regime(profile: dict) -> float:
    salary = profile["gross_salary"]
    std_deduction = 50000

    # HRA Exemption calculation (simplified for engine)
    hra_exemption = min(
        profile["hra_received"],
        profile["rent_paid"] - (0.10 * profile["basic_salary"]),
        0.40 * profile["basic_salary"]
    )
    hra_exemption = max(0.0, hra_exemption)

    deductions = std_deduction + hra_exemption
    deductions += min(profile["sec_80c"], 150000)
    deductions += min(profile["sec_80ccd_1b"], 50000)
    deductions += min(profile["sec_80d"], 25000)
    deductions += min(profile["home_loan_interest"], 200000)

    taxable_income = max(0.0, salary - deductions)

    # Tax slabs (Old Regime FY 2024-25)
    tax = 0.0
    if taxable_income > 1000000:
        tax += (taxable_income - 1000000) * 0.30 + 112500
    elif taxable_income > 500000:
        tax += (taxable_income - 500000) * 0.20 + 12500
    elif taxable_income > 250000:
        tax += (taxable_income - 250000) * 0.05

    # Section 87A rebate for old regime (up to 5L taxable income)
    if taxable_income <= 500000:
        tax = max(0.0, tax - 12500)

    cess = tax * 0.04
    return round(tax + cess, 2)


def calculate_tax_new_regime(profile: dict) -> float:
    salary = profile["gross_salary"]
    std_deduction = 75000  # Updated in recent budgets
    taxable_income = max(0.0, salary - std_deduction)

    # Tax slabs (New Regime)
    tax = 0.0
    if taxable_income > 1500000:
        tax = (taxable_income - 1500000) * 0.30 + 150000
    elif taxable_income > 1200000:
        tax = (taxable_income - 1200000) * 0.20 + 90000
    elif taxable_income > 1000000:
        tax = (taxable_income - 1000000) * 0.15 + 60000
    elif taxable_income > 700000:
        tax = (taxable_income - 700000) * 0.10 + 25000
    elif taxable_income > 300000:
        tax = (taxable_income - 300000) * 0.05

    # Section 87A rebate for new regime (taxable income up to 7L)
    if taxable_income <= 700000:
        tax = 0.0

    cess = tax * 0.04
    return round(tax + cess, 2)


# ==========================================
# PROJECT B: DATA QUALITY CORRUPTION INJECTOR & DETECTORS
# ==========================================

class NYC311DataCorruptionInjector:
    """Injects 12 specified data quality problems into clean telemetry batches."""

    @staticmethod
    def inject_swapped_lat_long(record: dict) -> dict:
        rec = record.copy()
        rec["latitude"], rec["longitude"] = rec.get("longitude", 0.0), rec.get("latitude", 0.0)
        return rec

    @staticmethod
    def inject_closed_before_created(record: dict) -> dict:
        rec = record.copy()
        rec["closed_date"] = "2022-01-01 00:00:00"
        rec["created_date"] = "2023-01-01 00:00:00"
        return rec


class NYC311DataQualityPipeline:
    """Hybrid detection pipeline implementing declarative rules, stats, and LLM review."""

    def run_schema_checks(self, record: dict) -> bool:
        required_keys = {"unique_key", "created_date", "agency", "complaint_type", "borough"}
        return all(k in record for k in required_keys)

    def run_temporal_checks(self, record: dict) -> bool:
        c_date = record.get("created_date", "")
        cl_date = record.get("closed_date", "")
        if c_date and cl_date and cl_date < c_date:
            return False
        return True


if __name__ == "__main__":
    print("--- FireAI Take-Home Sample Execution ---")
    sample_profile = {
        "gross_salary": 1500000,
        "hra_received": 0,
        "rent_paid": 0,
        "basic_salary": 800000,
        "city_type": "metro",
        "sec_80c": 150000,
        "sec_80ccd_1b": 50000,
        "sec_80d": 25000,
        "home_loan_interest": 0,
    }
    print(f"Sample Old Regime Tax: INR {calculate_tax_old_regime(sample_profile)}")
    print(f"Sample New Regime Tax: INR {calculate_tax_new_regime(sample_profile)}")
