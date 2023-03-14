from django.contrib import admin
from listings.models import Band
from listings.models import Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


admin.site.register(Band, BandAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'band', 'year', 'sold')


admin.site.register(Listing, ListingAdmin)
