from django.db import models
from django.contrib.auth.models import User


class OneshirtUser(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fname = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    team = models.IntegerField()


class Item(models.Model):
    item_types = (
    ('ts', "T-Shirt"),
    ('hat', "Hat"),
    )

    owner = models.ForeignKey(OneshirtUser, on_delete=models.CASCADE)
    team = models.IntegerField()
    classification = models.CharField(max_length=10, choices=item_types)
    description = models.TextField()
    available = models.BooleanField(default=True)


class Trade(models.Model):
    statuses = (
    ('a', 'Accepted'),
    ('d', 'Denied'),
    ('p', 'Pending')
    )
    give = models.ManyToManyField(Item, related_name="trade_item_given")
    take = models.ManyToManyField(Item, related_name="trade_item_gotten")
    status = models.CharField(max_length=10, choices=statuses, default='p')
