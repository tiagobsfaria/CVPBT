from datetime import datetime, timedelta, time
from django.db.models import Q

def get_slots(campo, selected_date):
    day_of_week = selected_date.strftime('%A')

    # Get the opening and closing times for the selected day
    opening_time_field = campo.get_opening_time_field(day_of_week)
    closing_time_field = campo.get_closing_time_field(day_of_week)

    if opening_time_field is None or closing_time_field is None:
        print("Opening or closing time not set for the selected day.")
        return []  # Return an empty list if opening or closing time is not set for the selected day

    # Calculate available slots
    slot_duration = timedelta(hours=1)
    current_time = datetime.combine(selected_date, opening_time_field)
    end_time = datetime.combine(selected_date, closing_time_field)

    # Get already booked slots for the given campo and date
    booked_slots = campo.reserva_set.filter(date=selected_date)

    booked_slots_time_ranges = [(slot.start_time, slot.end_time) for slot in booked_slots]

    slots = []
    while current_time + slot_duration <= end_time:
        slot_start_time = current_time.time()
        slot_end_time = (current_time + slot_duration).time()

        # Check if the slot is not booked
        if all(
            slot_end_time <= booked_start_time or slot_start_time >= booked_end_time
            for booked_start_time, booked_end_time in booked_slots_time_ranges
        ):
            slots.append({
                'start_time': slot_start_time.strftime('%H:%M'),  # Format time as string
                'end_time': slot_end_time.strftime('%H:%M'),
            })

        current_time += slot_duration

    return slots
