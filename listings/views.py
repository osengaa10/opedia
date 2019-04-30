from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import journal_choices, rating_choices, keyword_match_choices
from django.db.models import Q

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)



def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)



def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        print(keywords)
        if keywords:
            #queryset_list = queryset_list.filter(description__icontains=keywords) # finds a matching word in the abstract (not case sensitive)
            queryset_list = queryset_list.filter(Q(description__icontains=keywords) | Q(abstract__icontains=keywords))#

    context = {
        'keyword_match_choices': keyword_match_choices,
        'rating_choices': rating_choices,
        'journal_choices': journal_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
