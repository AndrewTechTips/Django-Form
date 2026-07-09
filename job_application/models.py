from django.db import models


class JobApplication(models.Model):

    class OccupationChoices(models.TextChoices):
        EMPLOYED = "employed", "Employed"
        UNEMPLOYED = "unemployed", "Unemployed"
        SELF_EMPLOYED = "self-employed", "Self-Employed"
        STUDENT = "student", "Student"

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()

    occupation = models.CharField(
        max_length=20,
        choices=OccupationChoices.choices,
        default=OccupationChoices.STUDENT,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
