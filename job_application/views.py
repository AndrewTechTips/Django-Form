from django.shortcuts import render
from forms import ApplicationForm


def index(request):
    if request.method == "POST":
        form = ApplicationForm()
        first_name = form.cleaned_data.get("first_name", "")
        last_name = form.cleaned_data.get("last_name", "")
        email = form.cleaned_data.get("email", "")
        occupation = form.cleaned_data.get("occupation", "")
    return render(request, "index.html")
