# utils.py
from datetime import datetime, timedelta, time

def get_slots(campo, selected_date):
    day_of_week = selected_date.strftime('%A')

    print(f"Dia da semana escolhido {day_of_week}")

    # Get the opening and closing times for the selected day
    opening_time_field = campo.get_opening_time_field(day_of_week)
    closing_time_field = campo.get_closing_time_field(day_of_week)

    print(f"Abertura: {opening_time_field}")
    print(f"Fecho: {closing_time_field}")

    if opening_time_field is None or closing_time_field is None:
        print("Opening or closing time not set for the selected day.")
        return []  # Return an empty list if opening or closing time is not set for the selected day


    print(f"Selected Date: {selected_date}")

    # Calculate available slots
    slot_duration = timedelta(hours=1)
    current_time = datetime.combine(selected_date, opening_time_field)
    end_time = datetime.combine(selected_date, closing_time_field)

    slots = []
    while current_time + slot_duration <= end_time:
        slots.append({
            'start_time': current_time.time().strftime('%H:%M'),  # Format time as string
            'end_time': (current_time + slot_duration).time().strftime('%H:%M'),
        })
        current_time += slot_duration

    print("Slots:", slots)
    return slots
