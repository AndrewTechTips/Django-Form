from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get("first_name", "")
            last_name = form.cleaned_data.get("last_name", "")
            email = form.cleaned_data.get("email", "")
            date = form.cleaned_data.get("date", "")
            occupation = form.cleaned_data.get("occupation", "")

            # Store data in the db
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

    return render(request, "index.html")
