from flask import flash, session


def flash_error(error):
    session.pop('_flashes', None)
    flash(error, "error")


def flash_notification(notification):
    session.pop('_flashes', None)
    flash(notification, 'notification')
