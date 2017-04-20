from calendar import monthrange
from datetime import datetime, date
from random import randint

from django.shortcuts import render

from Crate.models import InterestGroup


def homepage(request):
    # Sets the end of the cycle date to be the last day of the month
    today = date.today()
    _, num_days = monthrange(today.year, today.month)
    end_of_month = datetime(today.year, today.month, num_days)
    # TODO: Set the end of the month as 1 minute before the start of the new month
    # Checks to see if end of the month is today
    if end_of_month == today:
        year = today.year
        next_month = (today.month + 1) % 12
        if next_month < today.month:
            year = today.year + 1
        _, num_days = monthrange(year, next_month)
        end_of_month = datetime(year, next_month, num_days)

    # Must use .all() to get an iterate (be able to convert to list)
    list_interest_groups = list(InterestGroup.objects.all())
    chosen_interest_groups = []
    if len(list_interest_groups) > 0:
        for _ in range(3):
            num = randint(0, len(list_interest_groups) - 1)
            chosen_interest_group = list_interest_groups[num]
            chosen_interest_groups.append(chosen_interest_group)
            list_interest_groups.remove(chosen_interest_group)

    return render(request, 'homepage.html', {'cycle_date': end_of_month,
                                             'interest_groups': chosen_interest_groups})
