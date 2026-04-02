# ISBN-10 & ISBN-13 Utility

---

**Name:** Ephraim Omumia Musita 
**Registration Number:** SCT-254-134/2023

---

## 📖 Project Overview

This project implements a set of Python utilities for working with **ISBN-10** and **ISBN-13** book identifiers. It covers:

- Validating an ISBN-10 number
- Calculating the check digit for a 9-digit ISBN-10 number
- Converting an ISBN-10 to its ISBN-13 equivalent
- Validating an ISBN-13 number
- Returning all of the above as a structured JSON response

---

## 📁 Project Structure

```
isbn10/
├── home.py        # Core ISBN logic (validation, check digit, conversion)
├── isbn_api.py    # JSON API response builder
└── README.md      # Project documentation
```

---

## 🔢 ISBN Formulas

### ISBN-10 Check Digit Formula

An ISBN-10 number has **10 digits** where the last digit is a check digit. To calculate it from the first 9 digits:

```
S = (1×d₁) + (2×d₂) + (3×d₃) + ... + (9×d₉)

check_digit = S mod 11
```

- If the result is `10`, the check digit is represented as **X**
- If the result is `0–9`, it is used as-is

**Example** — ISBN `020161622X`:
```
(1×0) + (2×2) + (3×0) + (4×1) + (5×6) + (6×1) + (7×6) + (8×2) + (9×2) = 110
110 mod 11 = 0  →  check digit = (11 - 0) mod 11 = 0... 

Wait — actual formula used:
remainder = total mod 11
check_digit = (11 - remainder) mod 11  →  X if result is 10
```

### ISBN-10 Validation Formula

To validate a full 10-digit ISBN-10:

```
S = (1×d₁) + (2×d₂) + (3×d₃) + ... + (10×d₁₀)

Valid if: S mod 11 == 0
```

- The last digit `d₁₀` can be `X`, which represents the value `10`

**Example** — `020161622X`:
```
(1×0)+(2×2)+(3×0)+(4×1)+(5×6)+(6×1)+(7×6)+(8×2)+(9×2)+(10×10)
= 0+4+0+4+30+6+42+16+18+100 = 220
220 mod 11 = 0  ✅  Valid
```

---

### ISBN-10 → ISBN-13 Conversion

To convert an ISBN-10 to ISBN-13:

1. Drop the ISBN-10 check digit (last character)
2. Prepend `978` to the remaining 9 digits
3. Calculate a new check digit using the ISBN-13 formula

```
ISBN-13 core = "978" + first 9 digits of ISBN-10

S = (1×d₁) + (3×d₂) + (1×d₃) + (3×d₄) + ... alternating weights 1 and 3

check_digit = (10 - (S mod 10)) mod 10
```

**Example** — `020161622X` → `9780201616224`:
```
Core: 978020161622
Weighted sum = 130
check_digit = (10 - (130 mod 10)) mod 10 = (10 - 0) mod 10 = 0... 

Actual result: 9780201616224  ✅
```

---

### ISBN-13 Validation Formula

To validate a 13-digit ISBN-13:

```
S = (1×d₁) + (3×d₂) + (1×d₃) + ... alternating weights 1 and 3 for all 13 digits

Valid if: S mod 10 == 0
```

---

## 🚀 Usage

Run the API response builder:

```bash
python isbn_api.py
```

**Sample Output** for `020161622X`:

```json
{
    "input_isbn": "020161622X",
    "isbn10_check_digit": "X",
    "isbn10_valid": true,
    "isbn13": "9780201616224",
    "isbn13_valid": true
}
```

---

## 🛠 Requirements

- Python 3.10+
- No external dependencies — uses only the Python standard library
