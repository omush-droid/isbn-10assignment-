import json
from home import calculate_isbn10_check_digit, is_valid_isbn10, isbn10_to_isbn13, is_valid_isbn13

def isbn_api_response(isbn):
    isbn = isbn.replace("-", "").upper()
    
    response = {
        "input_isbn": isbn,
        "isbn10_check_digit": calculate_isbn10_check_digit(isbn[:9]) if len(isbn) >= 9 else None,
        "isbn10_valid": is_valid_isbn10(isbn) if len(isbn) == 10 else None,
        "isbn13": isbn10_to_isbn13(isbn) if len(isbn) == 10 else None,
        "isbn13_valid": is_valid_isbn13(isbn10_to_isbn13(isbn)) if len(isbn) == 10 else None
    }
    
    return json.dumps(response, indent=4)

print(isbn_api_response("020161622X"))