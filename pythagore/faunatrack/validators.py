from django.forms import ValidationError


def validate_latitude(value):
    if value < -90 or value > 90:
        raise ValidationError("La latitude doit être comprise entre -90 et 90.")
    
    
def validate_longitude(value):
    if value < -180 or value > 180:
        raise ValidationError("La longitude doit être comprise entre -180 et 180.")