from django.conf.urls import url

from .views import index, auth, search

app_name = 'trade'
urlpatterns = [
    # Index
    url(r'^$', index.index, name='index'),

    # Auth
    url(r'^login/$', auth.login, name='login'),

    #Search
    url(r'^search/$', search.search, name='search'),
]
