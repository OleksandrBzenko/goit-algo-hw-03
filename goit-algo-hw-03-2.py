import random


def get_numbers_ticket(min_num, max_num, quantity):
    if quantity>(max_num - min_num +1):
        raise ValueError("Qantity is larger tham range of numbers")
    return random.sample(range (min_num, max_num +1), quantity)
print("Your lottery ticket:", get_numbers_ticket(1, 49, 6))
print("Your lottery ticket:", get_numbers_ticket(1, 36, 5))


