
from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(email_address):
    # TODO consider instead inheriting from default email validator and overriding the domain checking part

    if not email_address or "@" not in email_address:
        raise ValidationError("Enter a Cabinet Office email address")

    domain_part = email_address.rsplit("@", 1)[1]

    if domain_part != "cabinetoffice.gov.uk":
        raise ValidationError("Enter a Cabinet Office email address")

    return True
    

class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()

