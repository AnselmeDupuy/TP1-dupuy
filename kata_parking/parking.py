from datetime import datetime
from math import ceil, floor

def check_duration_free_parking(duration_in_minutes: float, is_electric: bool) -> bool:
    if not isinstance(duration_in_minutes, (int, float)):
        raise TypeError("Invalid duration: must be a number")
    if duration_in_minutes < 0:
        raise ValueError("Invalid duration: must be a positive number")
    if is_electric and duration_in_minutes <= 60:
        return True
    if not is_electric and duration_in_minutes <= 30:
        return True
    return False

def calculate_parking_fee(duration_in_minutes: float, subscribed: bool, is_electric: bool) -> float:
    if not isinstance(duration_in_minutes, (int, float)):
        raise TypeError("Invalid duration: must be a number")
    if not isinstance(subscribed, bool):
        raise TypeError("Invalid subscribed status: must be a boolean")
    if not isinstance(is_electric, bool):
        raise TypeError("Invalid electric status: must be a boolean")
    if duration_in_minutes < 0:
        raise ValueError("Invalid duration: must be a positive number")

    free_minutes = 60 if is_electric else 30
    paid_minutes = max(0, duration_in_minutes - free_minutes)
    total_price = ceil(paid_minutes / 30) * 1.5

    if subscribed:
        total_price *= 0.6

    return total_price

def price_cap(price: float, duration_in_minutes: int, subscribed: bool) -> bool:
    if not isinstance(price, (int, float)):
        raise TypeError("Invalid price: must be a number")
    if not isinstance(duration_in_minutes, int):
        raise TypeError("Invalid duration: must be an integer")
    if price < 0 or duration_in_minutes < 0:
        raise ValueError("Invalid price: must be a positive number")
    if not isinstance(subscribed, bool):
        raise TypeError("Invalid subscribed status: must be a boolean")

    if duration_in_minutes / 1440 <= 1:
        if price <= 18:
            return True
    elif duration_in_minutes / 1440 <= 1 and subscribed:
        if price <= 18 * 0.6:
            return True
    elif duration_in_minutes / 1440 > 1:
        if price * (1 / (duration_in_minutes / 1440)) <= 18 * (duration_in_minutes / 1440):
            return True

    return False

def impound(duration_in_minutes: int) -> bool:
    if not isinstance(duration_in_minutes, int):
        raise TypeError("Invalid duration: must be an integer")
    if duration_in_minutes < 0:
        raise ValueError("Invalid duration: must be a positive number")

    if duration_in_minutes > 1440 * 3:
        return True

    return False

def check_duration(time_arrive: datetime, time_departure: datetime) -> int:
    return None

def check_price_at_time(duration_in_minutes: int, subscribed: bool) -> bool:
    return None