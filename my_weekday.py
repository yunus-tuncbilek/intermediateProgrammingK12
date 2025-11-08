# -----------------------------------------------------------
# Assignment: Recreate datetime.date(...).weekday()
# -----------------------------------------------------------
# Instructions:
# 1. Complete the is_leap_year() and my_weekday() functions.
# 2. Do NOT import datetime or calendar inside those functions.
# 3. Use your own logic to calculate the weekday.
# -----------------------------------------------------------

import datetime
import random

# --------------------------
# Step 1: Leap year function
# --------------------------
def is_leap_year(year):
    """
    Return True if year is a leap year, otherwise False.

    Rules:
    - A year is a leap year if it is divisible by 4,
      except for years divisible by 100,
      unless it is also divisible by 400.

    Examples:
    - 1998 is not a leap year
    - 1996 is a leap year
    - 2100 will not be a leap. (it is divisible by 100 but not by 400)
    - 2000 is a leap year.
    - 4200 is not a leap year.
    - 2004 is a leap year.
    """
    # TODO: implement this
    pass


# --------------------------
# Step 2: Optional Helper(s)
# --------------------------
def days_in_month(year, month):
    """Return the number of days in a given month of a given year."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30
    
# --------------------------
# Step 3: Weekday calculator
# --------------------------
def my_weekday(year, month, day):
    """
    Return the weekday of the given date as an integer:
    0 = Monday, 1 = Tuesday, ..., 6 = Sunday

    You may:
    - Use a known reference date (e.g., Jan 1, 1900 was a Monday)
    - Count the number of days between the given date and the reference
    - Use your is_leap_year() function when counting days
    """
    # TODO: implement this
    pass


# --------------------------
# Step 4: Unit Tests
# --------------------------

def run_tests():
    """Run a suite of tests comparing my_weekday to datetime.weekday."""

    # --- Basic known dates ---
    known_dates = [
        (2000, 1, 1),    # Saturday
        (1900, 1, 1),    # Monday
        (2020, 2, 29),   # Saturday (leap year)
        (2021, 3, 1),    # Monday
        (2025, 10, 21),  # Tuesday
    ]

    for y, m, d in known_dates:
        expected = datetime.date(y, m, d).weekday()
        got = my_weekday(y, m, d)
        assert got == expected, f"Failed for {y}-{m}-{d}: expected {expected}, got {got}"

    # --- Leap year tests ---
    leap_years = [1600, 2000, 2020, 2024]
    non_leaps = [1700, 1800, 1900, 2100]
    for y in leap_years:
        assert is_leap_year(y) is True, f"{y} should be leap year"
    for y in non_leaps:
        assert is_leap_year(y) is False, f"{y} should not be leap year"

    # --- Random tests ---
    for _ in range(1000):
        y = random.randint(1600, 2500)
        m = random.randint(1, 12)
        d = random.randint(1, days_in_month(y, m))
        expected = datetime.date(y, m, d).weekday()
        got = my_weekday(y, m, d)
        assert got == expected, f"Random test failed for {y}-{m}-{d}: expected {expected}, got {got}"

    print("✅ All tests passed!")


if __name__ == "__main__":
    run_tests()