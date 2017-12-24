from django.conf.urls import url

from .views import index, auth, search

app_name = 'trade'
urlpatterns = [
    # Index
    url(r'^$', index.index, name='index'),

    # Auth
    url(r'^login/$', auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^register/$', auth.register, name='register'),

    #Search
    url(r'^search/$', search.search, name='search'),
]
