from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["first_name", "last_name", "email", "date", "occupation"]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "John"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Doe"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "john.doe@example.com"}
            ),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "occupation": forms.RadioSelect(attrs={"class": "form-check-input"}),
        }
