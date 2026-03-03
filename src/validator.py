import re
from datetime import datetime

ALLOWED_CATEGORIES = [
    "Performance Update",
    "Research Insight",
    "Product Communication",
    "Marketing"
]


def validate_mobile(mobile: str) -> bool:
    """
    Validate mobile number (10–15 digits, optional + prefix)
    """
    return bool(re.match(r"^\+?\d{10,15}$", mobile))


def validate_datetime(schedule: str):
    """
    Validate datetime format: YYYY-MM-DD HH:MM
    Returns datetime object if valid, else None
    """
    try:
        parsed_dt = datetime.strptime(schedule, "%Y-%m-%d %H:%M")
        return parsed_dt
    except ValueError:
        return None


def validate_row(row: dict):
    """
    Validate entire row before compliance layer.
    Returns:
        (is_valid: bool, parsed_datetime: datetime or None, errors: list)
    """
    errors = []

    if not validate_mobile(row["Mobile"]):
        errors.append("Invalid mobile format")

    if not row["Message"] or not row["Message"].strip():
        errors.append("Message is empty")

    parsed_dt = validate_datetime(row["Schedule"])
    if not parsed_dt:
        errors.append("Invalid datetime format")
    elif parsed_dt < datetime.now():
        errors.append("Schedule is in the past")

    if row["Category"] not in ALLOWED_CATEGORIES:
        errors.append("Invalid category")

    is_valid = len(errors) == 0

    return is_valid, parsed_dt, errors