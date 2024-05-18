from django.core.exceptions import ValidationError

def validate_phone(value):

    if len(value) != 11:
        raise ValidationError('number phone invalid!!!')
    
    if not value.startswith('09'):
        raise ValidationError('number phone invalid!!! 09...')
    
    return value