from flask import render_template, redirect, url_for, abort
from flask_login import current_user
from . import main
from .forms import PostForm
from ..models import Post, User

@main.route('/', methods=["GET", "POST"])
def home():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.text.data, author=current_user._get_current_object())
        post.save()
        return redirect(url_for('.home'))
    posts = Post.objects
    return render_template('main/home.html', posts=posts, form=form)


@main.route('/user/<username>')
def profile(username):
    user = User.objects(username=username).first()
    if user is None:
        abort(404)
    posts = Post.objects(author=user)
    return render_template('main/profile.html', user=user, posts=posts)


@main.route('/post/<id>')
def post(id):
    post = Post.objects(id=id).first()
    if post is None:
        abort(404)
    return render_template('main/post.html', posts=[post])