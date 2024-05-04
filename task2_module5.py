import re
from typing import Callable

def sum_profit(text: str):
    pattern = r'\b\d+\.\d+\b'

    def generator_numbers():
        for match in re.finditer(pattern, text):
            yield float(match.group())

    numbers_generator = generator_numbers()

    total_profit = sum(numbers_generator)

    return total_profit


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_profit = sum_profit(text)
print("Загальний прибуток:", total_profit)
