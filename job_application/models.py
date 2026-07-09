from django.db import models
from django.core.validators import FileExtensionValidator


class JobApplication(models.Model):

    class OccupationChoices(models.TextChoices):
        EMPLOYED = "employed", "Employed"
        UNEMPLOYED = "unemployed", "Unemployed"
        SELF_EMPLOYED = "self-employed", "Self-Employed"
        STUDENT = "student", "Student"

    # Status is used internally
    class StatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        REVIEWED = "reviewed", "Reviewed"
        REJECTED = "rejected", "Rejected"
        HIRED = "hired", "Hired"

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField(verbose_name="Available start date")

    occupation = models.CharField(
        max_length=20,
        choices=OccupationChoices.choices,
        default=OccupationChoices.STUDENT,
    )

    resume = models.FileField(
        upload_to="resumes/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx"])],
        help_text="Upload your CV (PDF or Word format).",
    )

    status = models.CharField(
        max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"
