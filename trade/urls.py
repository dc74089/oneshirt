from django.urls import path

from .views import index, auth, search, item, trade

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

    # Trading
    path(r'trade/make', trade.new_trade, name='trade_new'),

    # Search
    path(r'search/', search.search, name='search'),
]
