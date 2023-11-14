import re


class MyClass:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        if not cls.is_valid_email(email):
            raise ValueError("Invalid email address format")

    @staticmethod
    def is_valid_email(email):
        # Regular expression for a valid email address
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(re.match(email_pattern, email))


try:
    obj = MyClass("user@example.com")
    print(f"Email validation successful. Email: {obj.email}")
except ValueError as e:
    print(f"Error: {e}")
