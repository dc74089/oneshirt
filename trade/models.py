import binascii
import os
from random import randint

from django.contrib.auth.models import User
from django.db import models


class FRCTeam(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    number = models.IntegerField()
    nickname = models.TextField()

    def __str__(self):
        return str(self.number)


class FRCComp(models.Model):
    compCode = models.CharField(max_length=30)
    shortName = models.TextField()
    longName = models.TextField()
    teams = models.ManyToManyField(FRCTeam)

    def __str__(self):
        return self.longName


class OneshirtUser(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fname = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    team = models.ForeignKey(FRCTeam, on_delete=models.SET_NULL, null=True, blank=True, unique=False)

    def __str__(self):
        if self.team:
            return "%s from %s" % (self.fname, self.team)
        else:
            return "%s (no team)" % self.fname


class PasswordResetRequest(models.Model):
    def gen_key():
        k = binascii.b2a_hex(os.urandom(15))
        while len(PasswordResetRequest.objects.filter(key=k)) != 0:
            k = binascii.b2a_hex(os.urandom(15))
        return k

    user = models.ForeignKey(OneshirtUser, on_delete=models.CASCADE)
    key = models.CharField(primary_key=True, max_length=30, default=gen_key)
    valid = models.BooleanField(default=True)

    def __str__(self):
        if self.valid:
            return "Valid reset for %s" % self.user
        else:
            return "Invalid reset for %s" % self.user


class Item(models.Model):
    item_types = (
        ('ts', "T-Shirt"),
        ('hat', "Hat"),
        ('zip', "Zip-Up Hoodie"),
        ('pull', "Pullover Hoodie"),
        ('swt', "Sweater"),
        ('pnt', "Pants"),
        ('sk', "Socks"),
        ('etc', "Doodad/Other"),
    )

    def generate_id():  # Generate an ID for an item
        id = randint(100, 1000000)
        while len(Item.objects.filter(id=id)) != 0:
            id = randint(100, 1000000)
        return id

    id = models.PositiveIntegerField(primary_key=True, default=generate_id, editable=False)
    owner = models.ForeignKey(OneshirtUser, on_delete=models.CASCADE)
    team = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    classification = models.CharField(max_length=10, choices=item_types)
    description = models.TextField()
    available = models.BooleanField(default=True)
    photo = models.ImageField(null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        if self.team > 0:
            if self.year and self.year > 0:
                return "%s %s (%s)" % (self.team, self.get_classification_display(), self.year)
            else:
                return "%s %s" % (self.team, self.get_classification_display())
        else:
            if self.year and self.year > 0:
                return "%s (%s, no team)" % (self.get_classification_display(), self.year)
            else:
                return "%s (no team)" % self.get_classification_display()


class Trade(models.Model):
    statuses = (
        ('a', 'Accepted'),
        ('d', 'Denied'),
        ('p', 'Pending'),
        ('c', 'Cancelled'),
    )
    requester = models.ForeignKey(OneshirtUser, null=False, blank=False, on_delete=models.CASCADE,
                                  related_name="trade_user_requester")
    recipient = models.ForeignKey(OneshirtUser, null=False, blank=False, on_delete=models.CASCADE,
                                  related_name="trade_user_recipient")
    give = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE, related_name="trade_item_given")
    take = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE, related_name="trade_item_gotten")
    status = models.CharField(max_length=10, choices=statuses, default='p')

    def __str__(self):
        return "%s offering %s for %s from %s" % (
            self.requester, str(self.give), str(self.take), self.recipient
        )
