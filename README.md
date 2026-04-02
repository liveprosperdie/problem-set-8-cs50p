# CS50P — Problem Set 8: Object-Oriented Programming

## Overview

This problem set introduces Object-Oriented Programming (OOP) in Python. It covers designing classes with constructors, properties, getters/setters, dunder methods, and using third-party libraries like `fpdf2` to generate real-world outputs.

---

## Problems

### 1. `jar.py` — Cookie Jar

A class-based implementation of a cookie jar.

**Class:** `Jar`

- `__init__(self, capacity=12)` — Initializes the jar with a given capacity (default 12). Raises `ValueError` if capacity is not a non-negative integer.
- `__str__(self)` — Returns a string of 🍪 emojis equal to the current number of cookies in the jar.
- `deposit(self, n)` — Adds `n` cookies to the jar. Raises `ValueError` if the deposit would exceed capacity.
- `withdraw(self, n)` — Removes `n` cookies from the jar. Raises `ValueError` if there aren't enough cookies.
- `capacity` (property) — Returns the jar's maximum capacity.
- `size` (property) — Returns the current number of cookies in the jar.

**Design choices:**
- Used `@property` with getters and setters for both `capacity` and `size` to enforce validation at the point of assignment rather than just at initialization.
- The actual values are stored in `_capacity` and `_size` (private by convention) to separate the property interface from the underlying data.

---

### 2. `test_jar.py` — Tests for Cookie Jar

Four pytest functions that test the `Jar` class thoroughly:

- `test_init` — Verifies default capacity and size on a fresh jar.
- `test_str` — Verifies the string representation at different fill levels.
- `test_deposit` — Tests that depositing works correctly and raises `ValueError` when over capacity.
- `test_withdraw` — Tests that withdrawing works correctly and raises `ValueError` when the jar is empty.

---

### 3. `seasons.py` — Seasons of Love

A program that calculates how old a user is in minutes based on their date of birth.

**How it works:**
- Prompts the user for their date of birth in `YYYY-MM-DD` format.
- Uses Python's built-in `datetime.date` class to subtract the birth date from today's date, yielding a `timedelta`.
- Converts the timedelta to total minutes using `total_seconds() / 60`.
- Uses the `inflect` library to convert the integer minute count into English words.
- Removes the word "and" from the output to match the style of the song from *Rent*.

**Functions:**
- `main()` — Handles input and output.
- `validate(dt)` — Parses and validates the date string, exits via `sys.exit` if invalid.
- `time(y, m, d)` — Computes and returns the age in minutes as an English string.

**Design choices:**
- Separated validation and calculation into distinct functions to make testing easier and keep `main()` clean.
- Used `date` objects rather than manual leap year math — the library handles all of that internally.

---

### 4. `shirtificate.py` — CS50 Shirtificate

A program that generates a personalized PDF shirtificate using `fpdf2`.

**How it works:**
- Prompts the user for their name.
- Creates an A4 portrait PDF with:
  - "CS50 Shirtificate" as a centered title at the top.
  - The `shirtificate.png` image centered on the page.
  - The user's name in white text overlaid on the shirt.
- Saves the output as `shirtificate.pdf`.

**Design choices:**
- Used `FPDF` directly rather than subclassing it, since no custom header/footer logic was needed.
- Positioned text over the image using `set_y()` and `set_text_color(255, 255, 255)` to achieve the white-on-shirt effect.
- Kept the structure simple inside a single `main()` function since the PDF generation is linear with no branching logic.

---

## Libraries Used

- `inflect` — English word conversion for numbers
- `fpdf2` — PDF generation

Install with:
```
pip install inflect fpdf2
```
