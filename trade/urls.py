from django.urls import path

from .views import index, auth, search, item, trade, admin

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

    # Items
    path(r'item/<int:id>/', item.view, name='item_view'),
    path(r'item/add/', item.new, name='item_add'),
    path(r'item/<int:id>/relist/', item.relist, name='item_relist'),

    # Trading
    path(r'trade/make', trade.new_trade, name='trade_new'),
    path(r'trade/accept', trade.accept, name='trade_accept'),

    # Search
    path(r'search/', search.search, name='search'),
    path(r'search/do', search.do_search, name='search_do'),

    # Admin
    path(r'admin/', admin.home, name='admin_home'),
    path(r'admin/verify/<int:id>/', admin.verify, name='admin_verify'),
    path(r'admin/delete/<int:id>/', admin.delete, name='admin_delete'),
    path(r'test/', admin.test),
]
