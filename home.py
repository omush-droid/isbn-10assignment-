
#validate isbn-10 number
def is_valid_isbn10(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    total = 0

    for i in range(10):
        if i == 9 and isbn[i] == "X":
            value = 10
        else:
            if not isbn[i].isdigit():
                return False
            value = int(isbn[i])

        total += (i + 1) * value

    return total % 11 == 0



# to check the validity of an ISBN-10 number and to calculate the check digit for a 9-digit ISBN-10 number.
def calculate_isbn10_check_digit(isbn9):
    isbn9 = isbn9.replace("-", "")

    if len(isbn9) != 9 or not isbn9.isdigit():
        return None

    total = 0

    for i in range(9):
        total += (i + 1) * int(isbn9[i])

    remainder = total % 11
    check_digit = (11 - remainder) % 11

    if check_digit == 10:
        return "X"
    else:
        return str(check_digit)
    


#isbn-10 to isbn-13 conversion
def isbn10_to_isbn13(isbn10):
    isbn10 = isbn10.replace("-", "").upper()
    if len(isbn10) != 10:
        return None

    # drop the ISBN-10 check digit
    isbn_core = isbn10[:9]
    isbn13_core = "978" + isbn_core  # prepend 978

    # calculate ISBN-13 check digit
    total = 0
    for i, digit in enumerate(isbn13_core):
        n = int(digit)
        weight = 1 if i % 2 == 0 else 3
        total += n * weight

    check_digit = (10 - (total % 10)) % 10
    return isbn13_core + str(check_digit)


#validate isbn-13 number

def is_valid_isbn13(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 13 or not isbn.isdigit():
        return False
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(isbn))
    return total % 10 == 0

