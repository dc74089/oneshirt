from django.urls import path

from .views import index, auth, search, item

app_name = 'trade'
urlpatterns = [
    # Index
    path(r'', index.index, name='index'),

    # Auth
    path(r'login/', auth.login, name='login'),
    path(r'logout/', auth.logout, name='logout'),
    path(r'register/', auth.register, name='register'),

    # Items
    path(r'item/<int:id>/', item.view, name='item_view'),
    path(r'item/add/', item.new, name='item_add'),

    # Search
    path(r'search/', search.search, name='search'),
]
