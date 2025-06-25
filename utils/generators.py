import random

class DataGenerator:
    @staticmethod
    def generate_random_5_digit():
        return str(random.randint(10000, 99999))

    def scroll_by_pixels(self, x=0, y=500):
        """
        Scroll the page by a specific number of pixels.
        :param x: horizontal pixels
        :param y: vertical pixels
        """
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

# utils/generators.py

import random
import string

def generate_vin_number(prefix="ABC"):
    """
    Generate a 17-character VIN:
    - First 3 are fixed alphabets (prefix)
    - Next 14 are random digits
    """
    if not prefix.isalpha() or len(prefix) != 3:
        raise ValueError("Prefix must be 3 alphabetic characters")

    digit_part = ''.join(random.choices(string.digits, k=14))
    return prefix.upper() + digit_part
