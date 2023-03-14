from datetime import datetime

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(
        request,
        'listings/band-list.html',
        {'bands': bands}
    )


def band_detail(request, band_id):
    # band = Band.objects.get(id=band_id)
    band = get_object_or_404(Band, id=band_id)
    return render(
        request,
        'listings/band-detail.html',
        {'band': band}
    )


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    listings_tab = Listing.objects.all()
    return render(
        request,
        'listings/listings.html',
        {'listings_tab': listings_tab}
    )


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(
        request,
        'listings/listing-detail.html',
        {'listing': listing}
    )


def contact(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data.get("name") or "anonyme"} via Merchex Contact Us from',
                message=form.cleaned_data.get('message'),
                from_email=form.cleaned_data.get('email'),
                recipient_list=['admin@merchex.xyz'],
            )
            request.session['email'] = form.cleaned_data.get('email')
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(
        request,
        'listings/contact.html',
        {'form': form}
    )


def email_sent(request):
    email = request.session.pop('email', None)
    return render(
        request,
        'listings/email-sent.html',
        {'email': email}
    )
