import re
import string
import random


def random_number(length):
    string_pool = string.ascii_letters + string.digits
    result = ""
    for i in range(length):
        result += random.choice(string_pool)
    return result


def regex_exists(pattern, value):
    p = re.compile(pattern)
    m = p.search(value)

    if m:
        return True
    return False
