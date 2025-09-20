from datetime import datetime, date


def get_days_from_today(day_str):

    try:
        between_day = datetime.strptime(day_str, "%Y-%m-%d").date()
        return(between_day - date.today()).days
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."
print(get_days_from_today("1989-08-02"))
print(get_days_from_today("2025-09-29"))
print(get_days_from_today("12-10-2027"))
    
    




