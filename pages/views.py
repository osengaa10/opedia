from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from researchers.models import Researcher
from listings.choices import journal_choices, rating_choices, keyword_match_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'keyword_match_choices': keyword_match_choices,
        'rating_choices': rating_choices,
        'journal_choices': journal_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all researchers
    researchers = Researcher.objects.order_by('-researcher_rating')
    # Get mvp
    mvp_researchers = Researcher.objects.all().filter(is_mvp=True)
    context = {
        'researchers': researchers,
        'mvp_researchers': mvp_researchers
    }
    return render(request, 'pages/about.html', context)
