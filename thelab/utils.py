import calendar
from .models import TeamMember, Absence


WEEK_DAY_DICT = dict(zip(range(7), calendar.day_abbr))
MONTHS_NAMES = list(calendar.month_name)


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
            html_output += f'<td class="{WEEK_DAY_DICT[week_day].lower()}"></td>'
        html_output += '</tr>'

        return html_output







