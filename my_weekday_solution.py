import datetime
import random

# --------------------------
# Leap year check
# --------------------------
def is_leap_year(year):
    """Return True if year is a leap year, otherwise False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# --------------------------
# Helper function
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
# Helper Function: Number of days between two dates
# --------------------------
def num_days_between(start, end):
    """
    Return the number of days between two dates (start and end).
    start and end are tuples of (year, month, day).

    Example: 
    start = (2020, 1, 1), end =(2020, 1, 31) -> returns 30 days

    if the start is after end, the dates are swapped.
    """
    total_days = 0
    y1, m1, d1 = start
    y2, m2, d2 = end

    # If the dates are the same
    if (y1, m1, d1) == (y2, m2, d2):
        return 0

    # Ensure start is before end
    if (y1, m1, d1) > (y2, m2, d2):
        y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1

    # Count days from start date to end date
    # Count full years
    for year in range(y1, y2):
        total_days += 366 if is_leap_year(year) else 365

    # Count full months in the end date year
    for month in range(1, m2):
        total_days += days_in_month(y2, month)

    # Add days in the last month of the end date
    total_days += d2

    # Subtract days in the first year
    for month in range(1, m1):
        total_days -= days_in_month(y1, month)

    # Subtract days in the first month of the start date
    total_days -= d1

    return total_days

# --------------------------
# Weekday function (no datetime)
# --------------------------
def my_weekday(year, month, day):
    """
    Return the weekday of the given date as an integer:
    0 = Monday, 1 = Tuesday, ..., 6 = Sunday.
    """
    # Reference: Jan 1, 1900 = Monday (weekday 0)
    ref_year, ref_month, ref_day = 1900, 1, 1
    ref_weekday = 0  # Monday

    # Calculate total days from reference date to the given date
    total_days = num_days_between((ref_year, ref_month, ref_day), (year, month, day))   

    # If the given date is before the reference date, adjust total_days
    if (year, month, day) < (ref_year, ref_month, ref_day):
        total_days = -total_days

    weekday = (ref_weekday + total_days) % 7
    return weekday


# --------------------------
# Tests
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
        (1600, 1, 1),    # Saturday (historical)
        (2100, 3, 1),    # Monday (not leap year)
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
