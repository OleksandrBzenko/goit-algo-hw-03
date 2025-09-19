from datetime import datetime, date


def get_day_of_today(day_str):
    between_day = datetime.strptime(day_str, "%Y-%m-%d").date()
    return(between_day - date.today()).days
print(get_day_of_today("1989-08-02"))
print(get_day_of_today("2025-09-29"))
    
    




