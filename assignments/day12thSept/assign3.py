import re

phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "(987) 654-3210",
    "(111) 222-3333"
]

pattern = r"^\(\d{3}\) \d{3}-\d{4}$"

for number in phone_numbers:
    if re.match(pattern, number):
        print(f"Valid: {number}")
