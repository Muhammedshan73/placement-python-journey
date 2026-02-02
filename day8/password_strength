# 1 generate random password
# 2 check password strength
# 3 count characters used in password
# 4 give a strength score using math
# 5 save the result in a file using os

import random
import string
import re
import math
import os
from collections import Counter

length = 10
characters = string.ascii_letters + string.digits + "@$!%*?&"
password = "".join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)

has_upper = bool(re.search(r"[A-Z]", password))
has_lower = bool(re.search(r"[a-z]", password))
has_digit = bool(re.search(r"\d", password))
has_special = bool(re.search(r"[@$!%*?&]", password))

char_count = Counter(password)


score = 0
if len(password) >= 8:
    score += 2
if has_upper:
    score += 2
if has_lower:
    score += 2
if has_digit:
    score += 2
if has_special:
    score += 2

strength_score = math.ceil(score)


if strength_score >= 8:
    strength = "Strong"
elif strength_score >= 5:
    strength = "Medium"
else:
    strength = "Weak"


if not os.path.exists("password_reports"):
    os.mkdir("password_reports")

file_path = os.path.join("password_reports", "password_report.txt")
file = open(file_path, "w")
file.write(f"Generated Password: {password}\n")
file.write(f"Strength Level: {strength}\n")
file.write(f"Strength Score: {strength_score}\n")
file.write("Character Count:\n")
for char, count in char_count.items():
    file.write(f"{char} : {count}\n")
file.close()

print("Password analysis saved successfully!")
