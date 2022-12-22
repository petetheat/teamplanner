from django.db import models


ABSENCE_CHOICES = (
    ("HO", "Home Office"),
    ("O", "Office"),
    ("V", "Vacation"),
    ("F", "Flex Time"),
    ("PL", "Parental Leave")
)


class TeamMember(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    initials = models.CharField(max_length=10)

    def __str__(self):
        return self.initials


class Absence(models.Model):
    teammember = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    starting_date = models.DateField()
    end_date = models.DateField()
    absence_type = models.CharField(choices=ABSENCE_CHOICES, max_length=200)
