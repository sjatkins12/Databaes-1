from django.shortcuts import render


# Create your views here.

def box_vote(request, box_id):
    return render(request, 'Crate/box_vote.html', {'box_id': box_id})
