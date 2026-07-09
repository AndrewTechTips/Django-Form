import csv
from django.contrib import admin
from .models import JobApplication
from django.http import HttpResponse


# Custom action for admin
@admin.action(description="Export selected applications to CSV")
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="job_applications.csv"'

    writer = csv.writer(response)

    # Write the header
    writer.writerow(
        ["First Name", "Last Name", "Email", "Available Date", "Occupation", "Status"]
    )

    for application in queryset:
        writer.writerow(
            [
                application.first_name,
                application.last_name,
                application.email,
                application.date,
                application.occupation,
                application.status,
            ]
        )

    return response


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation", "status")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation", "status")
    ordering = ("-created_at",)

    actions = [export_to_csv]


admin.site.register(JobApplication, JobApplicationAdmin)
