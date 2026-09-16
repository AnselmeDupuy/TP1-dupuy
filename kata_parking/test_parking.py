
from datetime import datetime

from parking import check_duration_free_parking

def test_check_duration_free_parking(duration_in_minutes : float, is_electric: bool) -> bool:
    assert check_duration_free_parking(25.5, False) == False
    assert check_duration_free_parking(30, False) == False
    assert check_duration_free_parking(31.0, False) == True
    assert check_duration_free_parking("a", False) == Exception("Invalid duration: must be a number")
    assert check_duration_free_parking(-5, False) == Exception("Invalid duration: must be a positive number")
    assert check_duration_free_parking(60, True) == True
    assert check_duration_free_parking(90, True) == False
    assert check_duration_free_parking(120, True) == False

def test_calculate_parking_fee(duration_in_minutes : float, subscribed: bool, is_electric: bool) -> float:
    assert calculate_parking_fee(25.5, False, False) == 0
    assert calculate_parking_fee(30, False, False) == 0
    assert calculate_parking_fee(31.0, False, False) == 1.5
    assert calculate_parking_fee("a", False, False) == Exception("Invalid duration: must be a number")
    assert calculate_parking_fee(-5, False, False) == Exception("Invalid duration: must be a positive number")
    assert calculate_parking_fee(90, False, False) == 1.5
    assert calculate_parking_fee(120, False, False) == 3.0
    assert calculate_parking_fee(25.5, True, False) == 0
    assert calculate_parking_fee(30, True, False) == 0
    assert calculate_parking_fee(31.0, True, False) == 1.5 * 0.6
    assert calculate_parking_fee(90, True, False) == 1.5 * 0.6
    assert calculate_parking_fee(120, True, False) == 3.0 * 0.6
    assert calculate_parking_fee(25.5, False, True) == 0
    assert calculate_parking_fee(60, False, True) == 0
    assert calculate_parking_fee(61.0, False, True) == 1.5
    assert calculate_parking_fee(61, True, True) == 1.5 * 0.6
    assert calculate_parking_fee(120, True, True) == 1.5 * 0.6
    assert calculate_parking_fee(121, True, True) == 3.0 * 0.6

def test_price_cap(price: float, duration_in_minutes: int, subscribed: bool) -> bool:
    assert price_cap(18, 30, False) == True
    assert price_cap(19, 1300, False) == False
    assert price_cap(5, 30, False) == True
    assert price_cap(19.5, 1600, False) == True
    assert price_cap(18, 80, True) == True
    assert price_cap(19, 1300, True) == False
    assert price_cap(5, 30, True) == True
    assert price_cap(19.5, 1600, True) == True
    assert price_cap(-5, 30, False) == Exception("Invalid price: must be a positive number")
    assert price_cap("a", 30, False) == Exception("Invalid price: must be a number")
    assert price_cap(18, -30, False) == Exception("Invalid duration: must be a positive number")
    assert price_cap(18, "a", False) == Exception("Invalid duration: must be a number")

def test_impound(duration_in_minutes: int ) -> bool:
    assert impound(30) == False
    assert impound(1500) == False
    assert impound(4320) == True
    assert impound(4320) == True
    assert impound(-5) == Exception("Invalid duration: must be a positive number")
    assert impound("a") == Exception("Invalid duration: must be a number")

def test_check_duration(time_arrive : datetime, time_departure : datetime) -> int :
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 2, 10, 30, 0)) == 30
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 2, 11, 0, 0)) == 60
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 2, 12, 30, 0)) == 150
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 3, 10, 0, 0)) == 1440
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 4, 10, 0, 0)) == 2880
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 1, 10, 0, 0)) == Exception("Invalid duration: departure time must be after arrival time")
    assert check_duration(datetime(2026, 9, 2, 10, 0, 0), datetime(2026, 9, 2, 10, 0, 0)) == Exception("Invalid duration: departure time must be after arrival time")

def test_check_price_at_time(time_arrive: datetime) -> float:
    
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0)) == 0
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0)) == 0
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0)) == 1.5
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0)) == 3.0
    assert check_price_at_time(datetime(2026, 9, 2, 10, 0, 0)) == 4.5
    assert check_price_at_time(datetime(12)) == Exception("Invalid time: must be a datetime object (YY, MM, DD, HH, MM)")
