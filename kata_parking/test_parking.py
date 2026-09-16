
from datetime import datetime
import pytest

from parking import check_duration_free_parking, calculate_parking_fee, price_cap, impound, check_duration, check_price_at_time

def test_check_duration_free_parking():
    assert check_duration_free_parking(25.5, False)
    assert check_duration_free_parking(30, False)
    assert not check_duration_free_parking(31.0, False)
    with pytest.raises(TypeError):
        check_duration_free_parking("a", False)
    with pytest.raises(ValueError):
        check_duration_free_parking(-5, False)
    assert check_duration_free_parking(60, True)
    assert not check_duration_free_parking(90, True)
    assert not check_duration_free_parking(120, True)

def test_calculate_parking_fee():
    assert calculate_parking_fee(25.5, False, False) == 0
    assert calculate_parking_fee(300, False, False) == 13.5
    assert calculate_parking_fee(350, False, False) == 16.5
    with pytest.raises(TypeError):
        calculate_parking_fee("a", False, False)
    with pytest.raises(ValueError):
        calculate_parking_fee(-5, False, False)
    assert calculate_parking_fee(90, False, False) == 3.0
    assert calculate_parking_fee(120, False, False) == 4.5
    assert calculate_parking_fee(25.5, True, False) == 0
    assert calculate_parking_fee(30, True, False) == 0
    assert calculate_parking_fee(31.0, True, False) == pytest.approx(0.9)
    assert calculate_parking_fee(90, True, False) == pytest.approx(1.8)
    assert calculate_parking_fee(120, True, False) == pytest.approx(2.7)
    assert calculate_parking_fee(25.5, False, True) == 0
    assert calculate_parking_fee(60, False, True) == 0
    assert calculate_parking_fee(61.0, False, True) == 1.5
    assert calculate_parking_fee(61, True, True) == pytest.approx(0.9)
    assert calculate_parking_fee(120, True, True) == pytest.approx(1.8)
    assert calculate_parking_fee(120, False, True) == 3.0
    assert calculate_parking_fee(121, False, True) == 4.5
    
def test_price_cap():
    assert  price_cap(18, 30, False)
    assert not price_cap(19, 1300, False)
    assert price_cap(5, 30, False)
    assert price_cap(19.5, 1600, False)
    assert price_cap(18, 80, True)
    assert not price_cap(19, 1300, True)
    assert price_cap(5, 30, True)
    assert price_cap(19.5, 1600, True)
    with pytest.raises(ValueError):
        price_cap(-5, 30, False)
    with pytest.raises(TypeError):
        price_cap("a", 30, False)
    with pytest.raises(ValueError):
        price_cap(18, -30, False)
    with pytest.raises(TypeError):
        price_cap(18, "a", False)

def test_impound():
    assert impound(30) is False
    assert impound(1500) is False
    assert impound(4321) is True
    assert impound(6000) is True
    with pytest.raises(ValueError):
        impound(-5)
    with pytest.raises(TypeError):
        impound("a")

def test_check_duration():
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 2, 10, 30, 0))
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 2, 11, 0, 0))
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 2, 12, 30, 0))
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 3, 10, 0, 0))
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 4, 10, 0, 0))
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 1, 10, 0, 0)) == Exception("Invalid duration: departure time must be after arrival time")
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 2, 10, 0, 0)) == Exception("Invalid duration: departure time must be after arrival time")

def test_check_price_at_time() -> None:
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0), True)
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0), False)
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0), True)
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0), False)
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0), True)
    assert check_price_at_time(datetime(12)) == Exception("Invalid time: must be a datetime object (YY, MM, DD, HH, MM)")
