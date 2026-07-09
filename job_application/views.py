from django.shortcuts import render, redirect

from .forms import JobApplicationForm
from django.contrib import messages
from django.core.mail import EmailMessage


def send_confirmation_email(application):
    subject = "Job Application Received"

    message_body = (
        f"Hi {application.first_name},\n\n"
        "We have successfully received your job application. "
        "Our team will review it and get back to you shortly.\n\n"
        "Thank you!"
    )

    email = EmailMessage(subject=subject, body=message_body, to=[application.email])

    email.send()


def index(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FIlES)

        if form.is_valid():
            # Save data to db
            application = form.save()

            send_confirmation_email(application)

            messages.success(request, "Ypur application was submitted successfully!")

            # Prevents form resubmission on refresh
            return redirect("index")
    else:
        form = JobApplicationForm()

    return render(request, "index.html", {"form": form})


def about(request):
    return render(request, "about.html")
