import os

import tbapy

from .models import Item, OneshirtUser, FRCTeam, FRCComp


def init_tba():
    tba = tbapy.TBA(os.getenv("TBA_KEY"))


def update_tba_teams():
    tba = tbapy.TBA(os.getenv("TBA_KEY"))
    teams = {}
    team_objects = {}

    for i in range(16):
        for team in tba.teams(i, 2018):
            print("Team %d: %s" % (team.team_number, team.nickname))

            q = FRCTeam.objects.filter(key=team.key)
            if len(q) > 0:
                t = q.first()
            else:
                t = FRCTeam()

            t.key = team.key
            t.number = team.team_number
            t.nickname = team.nickname

            t.save()

            teams[team.key] = team
            team_objects[team.key] = t

    for event in tba.events(2018):
        print(event.name)
        q = FRCComp.objects.filter(compCode=event.key)
        if len(q) > 0:
            e = q.first()
        else:
            e = FRCComp()

        e.compCode = event.key
        e.shortName = event.short_name
        e.longName = event.name
        e.save()

        for team in tba.event_teams(event.key, simple=True):
            try:
                t = FRCTeam.objects.filter(key=team.key).first()
                e.teams.add(t)
                e.save()
            except:
                print("Error adding %s to %s" % (team.nickname, e.short_name))


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
