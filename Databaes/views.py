from calendar import monthrange
from datetime import datetime, date
from random import randint

from django.shortcuts import render

from Crate.models import SellingCycle, Box, Item


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

    # Finds 3 random items to display on the homepage
    curr_selling_cycle = SellingCycle.objects.filter(cycle_date__lte=date.today()).order_by('-cycle_date').first()
    boxes = Box.objects.filter(sold_during__cycle_date=curr_selling_cycle.cycle_date)
    items = []
    for box in boxes:
        for item in Item.objects.filter(contained_in=box):
            items.append(item)
    display_items = []
    for _ in range(3):
        num = randint(0, len(items) - 1)
        chosen_item = items[num]
        display_items.append(chosen_item)
        items.remove(chosen_item)
    return render(request, 'homepage.html', {'cycle_date': end_of_month,
                                             'items': display_items})
