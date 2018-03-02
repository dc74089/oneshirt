import os

from django.core.mail import send_mail
from django.template.loader import render_to_string


def feedback_mail(message, user):
    plain = message + "\n\nPosted by %s, %s" % (user.fname, user.email)
    subject = "FRCShirt Feedback"
    send_mail(subject, plain, "FRCShirt<trading@mail.frcshirt.trade>"[os.getenv("ADMIN_EMAIL")])


# TODO: Fix html message not displaying in gmail
def trade_mail(trade):
    ctx = {'trade': trade}
    html = render_to_string('trade/email/trade_notification.html', ctx)
    plain = "Hey %s, you have a trade offer!\n\n%s offered you their %s for your %s. Go to https://frcshirt.trade/, " \
            "log in, and select 'My Items' to view or accept the offer." % (
                trade.take.owner.fname, trade.give.owner, trade.give, trade.take
            )
    subject = "Trade offer for your %s" % trade.take

    send_mail(subject, plain, "FRCShirt<trading@mail.frcshirt.trade>", [trade.take.owner.email])


def trade_accepted_mail(trade):
    ctx = {'trade': trade}

    # TODO: Find meetup and insert into ctx

    html = render_to_string('trade/email/trade_accepted.html', ctx)
    plain = "Hey %s!\n\n%s accepted your trade offer! They want to trade your %s for their %s. You can get in touch " \
            "with them at %s to coordinate the trade. " % (
                trade.give.owner.fname, trade.take.owner, trade.give, trade.take, trade.take.owner.email
            )
    subject = "Trade offer accepted!"

    send_mail(subject, plain, "FRCShirt<trading@mail.frcshirt.trade>", [trade.give.owner.email])


def trade_cancelled_by_giver(trade):
    ctx = {'trade': trade}

    html = None
    plain = "Hey %s,\n\n%s just marked the trade of your %s for their %s as cancelled. Reach out to them if you think " \
            "this is an error. If you'd like to relist your %s, go to frcshirt.trade, click My Items and click " \
            "relist on its item page" % (
                trade.take.owner.fname, trade.give.owner, trade.take, trade.give, trade.take
            )
    subject = "Trade offer cancelled"

    send_mail(subject, plain, "FRCShirt<trading@mail.frcshirt.trade>", [trade.take.owner.email])


def trade_cancelled_by_taker(trade):
    ctx = {'trade': trade}

    html = None
    plain = "Hey %s,\n\n%s just marked the trade of your %s for their %s as cancelled. Reach out to them if you think " \
            "this is an error. If you'd like to relist your %s, go to frcshirt.trade, click My Items and click " \
            "relist on its item page" % (
                trade.give.owner.fname, trade.take.owner, trade.give, trade.take, trade.give
            )
    subject = "Trade offer cancelled"

    send_mail(subject, plain, "FRCShirt<trading@mail.frcshirt.trade>", [trade.give.owner.email])
