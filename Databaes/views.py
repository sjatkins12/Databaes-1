from calendar import monthrange
from datetime import datetime, date

from django.shortcuts import render


def homepage(request):
    today = date.today()
    _, num_days = monthrange(today.year, today.month)
    end_of_month = datetime(today.year, today.month, num_days)
    if end_of_month == today:
        year = today.year
        next_month = (today.month + 1) % 12
        if next_month < today.month:
            year = today.year + 1
        _, num_days = monthrange(year, next_month)
        end_of_month = datetime(year, next_month, num_days)
    return render(request, 'homepage.html', {'cycle_date': end_of_month})
