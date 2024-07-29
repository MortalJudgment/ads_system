import re
def validate_user_input(name, dob, email, interests):
    if not name or not dob or not email or len(interests) < 2:
        return False
    return True

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_age(age):
    return isinstance(age, int) and age > 0
