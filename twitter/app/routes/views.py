from flask import session, render_template, redirect, url_for
from . import routes
from .forms import SignUpForm
from ..models import User


@routes.route('/', methods=["GET", "POST"])
def home():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user is None:
            user = User()
            user.username = form.username.data
            user.email = form.email.data
            user.password = form.password.data
            user.save()
            session['known'] = False
        else:
            session['known'] = True
        session['username'] = form.username.data
        form.username.data = ''
        return redirect(url_for('.home'))
    return render_template('home.html', name=session.get('username'), form=form, known=session.get('known', False))