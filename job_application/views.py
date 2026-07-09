import os

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import JobApplicationForm
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives


def send_confirmation_email(application):
    subject = "Application Received - Confirmation"

    context = {f"first-name": application.first_name}
    html_content = render_to_string("emails/confirmation_email.html", context)

    # Fall back text
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=subject, body=text_content, to=[application.email]
    )

    email.attach_alternative(html_content, "text/html")
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


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Send the mail to the admin
        subject = f"New Contact Inquiry from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        email_message = EmailMessage(
            subject=subject, body=body, to=[os.getenv("EMAIL")]
        )
        email_message.send()
        messages.success(
            request, "Thanks for reaching out! We will get back to you shortly."
        )

        return redirect("contact")

    return render(request, "contact.html")
