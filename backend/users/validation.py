from django.core.exceptions import ValidationError
from .models import UserAccount

def custom_validation(data):
    email = data['email'].strip()
    password = data['password'].strip()
    phone_no = data['phone_no'].strip()
    
    if not email or UserAccount.objects.filter(email=email).exists():
        raise ValidationError("Email already exists")
    
    if not password or len(password) < 8:
        raise ValidationError('Password must be at least of length eight')
    
    if not phone_no or len(phone_no) < 10:
        raise ValidationError("Phone number is invalid.")
    return data

def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError("Please enter your Email address!")
    if not '@' in str(data["email"]):
        raise ValidationError("Invalid Email Address!")
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError("Please Enter Password!")
    return True
