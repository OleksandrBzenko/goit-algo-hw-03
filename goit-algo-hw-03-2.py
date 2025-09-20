import random


def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or quantity > (max_num - min_num + 1):
     return [] 
    return sorted(random.sample(range (min_num, max_num +1), quantity))
print("Your lottery ticket:", get_numbers_ticket(1, 49, 6))
print("Your lottery ticket:", get_numbers_ticket(1, 36, 5))
print("Your lottery ticket:", get_numbers_ticket(10, 4, 5))


