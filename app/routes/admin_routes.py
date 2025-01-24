from flask import render_template, session, Blueprint

admin = Blueprint('admin', __name__)


@admin.route('/privacy')
def privacy():
    return render_template("privacy.html")


@admin.route('/service')
def service():
    return render_template("service.html")
