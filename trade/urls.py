from django.conf.urls import url

from .views import index, auth, search, listing

app_name = 'trade'
urlpatterns = [
    # Index
    url(r'^$', index.index, name='index'),

    # Auth
    url(r'^login/$', auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^register/$', auth.register, name='register'),

    #Listings
    url(r'^listing/new/$', listing.new, name='listing_new'),

    #Search
    url(r'^search/$', search.search, name='search'),
]
