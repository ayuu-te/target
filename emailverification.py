# email_validator.py
import re

def is_valid_email(email):
    """
    Checks if a given email address is valid using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # A regular expression pattern for validating email addresses.
    # This pattern is based on RFC 5322 and is widely used for general validation.
    # It checks for a few things:
    # 1. An optional quoted string or a sequence of one or more "word" characters, dots, or hyphens.
    # 2. An '@' symbol.
    # 3. A domain name that can be composed of multiple parts separated by dots.
    # 4. A top-level domain (e.g., .com, .org, .co.uk) with a length of at least 2 characters.
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # The re.fullmatch() function returns a match object if the entire string matches the pattern,
    # otherwise it returns None.
    if re.fullmatch(email_regex, email):
        return True
    else:
        return False

# Example usage of the function
if __name__ == "__main__":
    test_emails = [
        "test@example.com",
        "john.doe123@sub.domain.co.uk",
        "invalid-email",
        "another@.com",
        "test@invalid@domain.com",
        "test@example.a", # Invalid TLD
        "valid_email@test.com"
    ]
    
    print("Checking the following email addresses for validity:")
    for email in test_emails:
        if is_valid_email(email):
            print(f"'{email}': is a valid email address.")
        else:
            print(f"'{email}': is NOT a valid email address.")
