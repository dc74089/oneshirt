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

    i = Item()
    i.id = 254
    i.owner = OneshirtUser.objects.get(django_user__username='test')
    i.team = 254
    i.year = 2016
    i.classification = Item.item_types[0][0]
    i.description = "A 254 Shirt. Blue. Shiny."
    i.save()
