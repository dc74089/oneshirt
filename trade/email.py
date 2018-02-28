from django.core.mail import send_mail
from django.template.loader import render_to_string


# TODO: Fix html message not displaying in gmail
def trade_mail(trade):
    ctx = {'trade': trade}
    html = render_to_string('trade/email/trade_notification.html', ctx)
    plain = "Hey %s, you have a trade offer!\n\n%s offered you their %s for your %s" % (
        trade.take.owner.fname, trade.give.owner, trade.give, trade.take
    )
    subject = "Trade offer for your %s" % trade.take

    send_mail(subject, plain, "webmaster@mail.frcshirt.trade", [trade.take.owner.email])


def trade_accepted_mail(trade):
    ctx = {'trade': trade}

    # TODO: Find meetup and insert into ctx

    html = render_to_string('trade/email/trade_accepted.html', ctx)
    plain = "Hey %s, %s accepted your trade offer! They want to trade your %s for their %s. You can get in touch with " \
            "them at %s to coordinate the trade. " % (
                trade.give.owner.fname, trade.take.owner, trade.give, trade.take, trade.take.owner.email
            )
    subject = "Trade offer accepted!"

    send_mail(subject, plain, "webmaster@mail.frcshirt.trade", [trade.give.owner.email])
