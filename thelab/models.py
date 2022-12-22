from django.db import models


class TeamMember(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    initials = models.CharField(max_length=10)

    def __str__(self):
        return self.initials
