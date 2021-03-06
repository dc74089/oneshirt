from django.urls import path

from . import startup
from .views import index, auth, search, item, trade, admin, api

app_name = 'trade'
urlpatterns = [
    # Index
    path(r'', index.index, name='index'),
    path(r'about/', index.about, name='index_about'),
    path(r'mine/', index.mine, name='items_mine'),

    # Auth
    path(r'login/', auth.login, name='login'),
    path(r'logout/', auth.logout, name='logout'),
    path(r'register/', auth.register, name='register'),
    path(r'login/forgot/', auth.forgot, name='auth_forgot'),
    path(r'login/reset/', auth.reset, name='auth_reset'),

    # Items
    path(r'item/<int:id>/', item.view, name='item_view'),
    path(r'item/add/', item.new, name='item_add'),
    path(r'item/<int:id>/relist/', item.relist, name='item_relist'),

    # Trading
    path(r'trade/make', trade.new_trade, name='trade_new'),
    path(r'trade/accept', trade.accept, name='trade_accept'),
    path(r'trade/decline', trade.decline, name='trade_decline'),

    # Search
    path(r'search/', search.search, name='search'),
    path(r'search/do', search.do_search, name='search_do'),

    # Admin
    path(r'admin/', admin.home, name='admin_home'),
    path(r'admin/verify/<int:id>/', admin.verify, name='admin_verify'),
    path(r'admin/delete/<int:id>/', admin.delete, name='admin_delete'),
    path(r'feedback/', admin.feedback, name='admin_feedback'),
    path(r'test/', admin.test),

    # API
    path(r'api/all', api.all_items, name='api_all'),
    path(r'api/search', api.search, name='api_search'),
]
