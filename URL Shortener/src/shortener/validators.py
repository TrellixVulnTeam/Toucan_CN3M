__author__ = 'Alkesh'
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()
    reg_value =  value

    if 'http' in reg_value:
        new_value = reg_value

    else:
        new_value = "http://" + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid URL")

    return new_value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("Invalid URL because of no .com")
    return value