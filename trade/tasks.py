from .models import Item, OneshirtUser


def create_sample_items():
    i = Item()
    i.id = 233
    i.owner = OneshirtUser.objects.get(django_user__username='dc74089')
    i.team = 233
    i.year = 2017
    i.classification = Item.item_types[0][0]
    i.description = "A pink Pink shirt."

    i.save()
