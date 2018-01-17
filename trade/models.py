from random import randint

from django.contrib.auth.models import User
from django.db import models


class OneshirtUser(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fname = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    team = models.IntegerField()

    def __str__(self):
        return "%s from %s" % (self.fname, self.team)


class Item(models.Model):
    item_types = (
        ('ts', "T-Shirt"),
        ('hat', "Hat"),
        ('etc', "Doodad"),
    )

    def generate_id():  # Generate an ID for an item
        id = randint(100, 1000000)
        while len(Item.objects.filter(id=id)) != 0:
            id = randint(100, 1000000)
        return id

    #  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.PositiveIntegerField(primary_key=True, default=generate_id, editable=False)
    owner = models.ForeignKey(OneshirtUser, on_delete=models.CASCADE)
    team = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    classification = models.CharField(max_length=10, choices=item_types)
    description = models.TextField()
    available = models.BooleanField(default=True)
    photo = models.ImageField(null=True)


class Trade(models.Model):
    statuses = (
        ('a', 'Accepted'),
        ('d', 'Denied'),
        ('p', 'Pending')
    )
    give = models.ManyToManyField(Item, related_name="trade_item_given")
    take = models.ManyToManyField(Item, related_name="trade_item_gotten")
    status = models.CharField(max_length=10, choices=statuses, default='p')
