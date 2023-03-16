from datetime import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm


def band_list(request):
    bands = Band.objects.all()
    return render(
        request,
        'listings/band-list.html',
        {'bands': bands}
    )


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(
        request,
        'listings/band-create.html',
        {'form': form}
    )


def band_change(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, band)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(
        request,
        'listings/band-change.html',
        {
            'id': band_id,
            'form': form
        }
    )


def band_delete(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    if request.method == 'POST':
        band.delete()
        messages.success(request, 'Groupe supprimé avec succès!')
        return redirect('bands')
    return render(
        request,
        'listings/band-delete.html',
        {
            'id': band_id,
            'band': band
        }
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


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(
        request,
        'listings/listing-create.html',
        {'form': form}
    )


def listing_change(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', listing_id)
    else:
        form = ListingForm(instance=listing)
    return render(
        request,
        'listings/listing-change.html',
        {
            'id': listing_id,
            'form': form
        }
    )


def listing_delete(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Annonce supprimée avec succès!')
        return redirect('listings')
    return render(
        request,
        'listings/listing-delete.html',
        {
            'id': listing_id,
            'listing': listing
        }
    )


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(
        request,
        'listings/listing-detail.html',
        {'listing': listing}
    )


def contact(request):
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
