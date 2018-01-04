from django.conf.urls import url

from .views import index, auth, search, item

app_name = 'trade'
urlpatterns = [
    # Index
    url(r'^$', index.index, name='index'),

    # Auth
    url(r'^login/$', auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^register/$', auth.register, name='register'),

    #Items
    url(r'^item/<uuid:id>/$', item.view, name='item_view'),
    url(r'^item/add/$', item.new, name='item_add'),

    #Search
    url(r'^search/$', search.search, name='search'),
]
