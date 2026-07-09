from datetime import timedelta
from django.utils import timezone
from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["first_name", "last_name", "email", "date", "occupation", "resume"]

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
            "occupation": forms.RadioSelect(),
            "resume": forms.FileInput(
                attrs={"class": "form-control", "accept": ".pdf,.doc,.docx"}
            ),
        }

    def clean_email(self):
        # Custom validation for emails (blocks new app if one already exists within the last 30 days)
        email = self.cleaned_data.get("email")
        thirty_days_ago = timezone.now() - timedelta(days=30)

        recent_application = JobApplication.objects.filter(
            email=email, created_at__gte=thirty_days_ago
        ).exists()

        if recent_application:
            raise forms.ValidationError(
                "You have already applied within the last 30 days. Please wait before applying again."
            )

        return email
