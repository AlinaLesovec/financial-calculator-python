import pytest
from calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax,
)

# ===== SIMPLE INTEREST =====

def test_simple_interest_basic():
    assert calculate_simple_interest(1000, 10, 2) == 200
    assert calculate_simple_interest(500, 5, 4) == 100


def test_simple_interest_zero():
    assert calculate_simple_interest(0, 10, 5) == 0
    assert calculate_simple_interest(1000, 0, 5) == 0


def test_simple_interest_negative():
    with pytest.raises(ValueError):
        calculate_simple_interest(-100, 10, 1)


# ===== COMPOUND INTEREST =====

def test_compound_interest_basic():
    result = calculate_compound_interest(1000, 10, 2)
    assert round(result, 2) == 1210.0

    result = calculate_compound_interest(1000, 12, 1, n=4)
    assert round(result, 2) == 1125.49


def test_compound_interest_zero():
    assert calculate_compound_interest(0, 10, 2) == 0


def test_compound_interest_invalid():
    with pytest.raises(ValueError):
        calculate_compound_interest(-1000, 10, 2)

    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 10, 2, n=0)


# ===== TAX =====

def test_tax_basic():
    assert calculate_tax(1000, 10) == 100
    assert calculate_tax(500, 20) == 100


def test_tax_zero():
    assert calculate_tax(0, 10) == 0
    assert calculate_tax(1000, 0) == 0


def test_tax_invalid():
    with pytest.raises(ValueError):
        calculate_tax(1000, -5)

    with pytest.raises(ValueError):
        calculate_tax(1000, 150)
