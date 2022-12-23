from django.contrib import admin
from .models import TeamMember, Absence, PublicHoliday


admin.site.register(TeamMember)
admin.site.register(Absence)
admin.site.register(PublicHoliday)
