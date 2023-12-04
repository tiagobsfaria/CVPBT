# utils.py
from datetime import datetime, timedelta

def get_slots(campo, selected_date):
    day_of_week = selected_date.weekday()

    # Get the opening and closing times for the selected day
    opening_time_field = campo.get_opening_time_field(day_of_week)
    closing_time_field = campo.get_closing_time_field(day_of_week)

    if opening_time_field is None or closing_time_field is None:
        return []  # Return an empty list if opening or closing time is not set for the selected day

    opening_time = getattr(campo, opening_time_field)
    closing_time = getattr(campo, closing_time_field)

    # Calculate available slots
    slot_duration = timedelta(hours=1)
    current_time = datetime.combine(selected_date, opening_time)
    end_time = datetime.combine(selected_date, closing_time)

    slots = []
    while current_time + slot_duration <= end_time:
        slots.append(current_time)
        current_time += slot_duration

    return slots