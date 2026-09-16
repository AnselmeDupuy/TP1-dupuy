from datetime import datetime

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
    return None

def price_cap(price: float, duration_in_minutes: int, subscribed: bool) -> bool:
    return None

def impound(duration_in_minutes: int) -> bool:
    return None

def check_duration(time_arrive: datetime, time_departure: datetime) -> int:
    return None

def check_price_at_time(duration_in_minutes: int, subscribed: bool) -> bool:
    return None