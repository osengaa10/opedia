from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    # check that its a post request
    if request.method == 'POST':
        # fetch listing_id that was declared in an input tag within listing.html
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        researcher_email = request.POST['researcher_email']

        # Check if user has made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already posted about this')
                return redirect('/listings/')

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, message=message, user_id=user_id)

        contact.save()

        # Send email
        # send_mail(
        #     'Research Message',
        #     'There has been in inquiry for ' + listing + '. Sign into the admin panel for more info',
        #     'aosenga@web3technology.com',
        #     [researcher_email, 'osengaa10@icloud.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Your message has been submitted')

        # return redirect('/listings/'+listing_id)
        return redirect('/listings/')