import calendar
from .models import TeamMember, Absence, PublicHoliday
import datetime


WEEK_DAY_DICT = dict(zip(range(7), calendar.day_abbr))
MONTHS_NAMES = list(calendar.month_name)
ABSENCE_DICT = {
    "HO": "home",
    "O": "office",
    "V": "vac",
    "F": "flex",
    "PL": "parental"
}


class Calendar:
    def __init__(self, year, month):
        n_days = calendar.monthrange(year, month)[1]
        self.n_days = n_days
        self.month = month
        self.year = year

    def formatmonth(self):
        html_output = f'<table border="0" cellpadding="0" cellspacing="0" class="month"><tbody>'
        html_output += f'<th colspan="{self.n_days}" class="month">{MONTHS_NAMES[self.month]} {self.year}</th>'
        html_output += '<tr>'
        html_output += '<th></th>'
        for d in range(self.n_days):
            week_day = calendar.weekday(self.year, self.month, d+1)
            html_output += f'<th class="{WEEK_DAY_DICT[week_day].lower()}">{WEEK_DAY_DICT[week_day]}</th>'
        html_output += '</tr><tr>'
        html_output += '<td></td>'
        for d in range(self.n_days):
            week_day = calendar.weekday(self.year, self.month, d+1)
            html_output += f'<td class="{WEEK_DAY_DICT[week_day].lower()}">{d+1}</td>'

        team_members = [tm.initials for tm in TeamMember.objects.all()]
        team_members.sort()

        for tm in team_members:
            html_output += self._format_team_member(tm)

        html_output += '</tr></tbody></table>'
        return html_output

    def _format_team_member(self, team_member):
        html_output = '<tr>'
        html_output += f'<td>{team_member}</td>'

        for d in range(self.n_days):
            week_day = calendar.weekday(self.year, self.month, d+1)
            date_check = datetime.date(self.year, self.month, d+1)

            absence = Absence.objects.filter(teammember__initials=team_member,
                                             starting_date__lte=date_check,
                                             end_date__gte=date_check)

            pub_holiday = PublicHoliday.objects.filter(date=date_check)
            if len(pub_holiday) == 1:
                html_output += f'<td class="pub">PH</td>'
            else:
                if len(absence) == 1:
                    if WEEK_DAY_DICT[week_day] in ['Sat', 'Sun']:
                        week_day_class = WEEK_DAY_DICT[week_day].lower()
                        absence_type = ""
                    else:
                        week_day_class = ABSENCE_DICT[absence[0].absence_type]
                        absence_type = absence[0].absence_type

                    html_output += f'<td class="{week_day_class}">{absence_type}</td>'
                else:
                    html_output += f'<td class="{WEEK_DAY_DICT[week_day].lower()}"></td>'
        html_output += '</tr>'

        return html_output







