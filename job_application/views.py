from django.shortcuts import render
from .forms import JobApplicationForm
from .models import JobApplication
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get("first_name", "")
            last_name = form.cleaned_data.get("last_name", "")
            email = form.cleaned_data.get("email", "")
            date = form.cleaned_data.get("date", "")
            occupation = form.cleaned_data.get("occupation", "")

            # Store data in the db
            JobApplication.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

            message_body = (
                f"A new job application was submitted. Thank you, \n{first_name}"
            )
            email_message = EmailMessage(
                "Form submission confirmation", message_body, to=[email]
            )
            email_message.send()

            messages.success(request, "Form submitted successfully")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
