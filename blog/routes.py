from blog.models import Post
from blog import db
from blog.forms import PostForm
from flask import Blueprint
from flask import render_template, request, session, flash, redirect, url_for
from blog.forms import LoginForm

bp = Blueprint("main", __name__)

@bp.route("/")
def homepage():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts)

@bp.route("/new-post", methods=["GET", "POST"])
@bp.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def post_form(post_id=None):
    post = Post.query.get_or_404(post_id) if post_id else Post()
    form = PostForm(obj=post)

    if form.validate_on_submit():
        form.populate_obj(post)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("main.homepage"))

    template = "edit_post.html" if post_id else "new_post.html"
    return render_template(template, form=form)


@bp.route("/delete-post/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("main.homepage"))

@bp.route("/login/", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   errors = None
   next_url = request.args.get('next')
   if request.method == 'POST':
       if form.validate_on_submit():
           session['logged_in'] = True
           session.permanent = True  # Use cookie to store session.
           flash('You are now logged in.', 'success')
           return redirect(next_url or url_for('index'))
       else:
           errors = form.errors
   return render_template("login_form.html", form=form, errors=errors)

@bp.route('/logout/', methods=['GET', 'POST'])
def logout():
   if request.method == 'POST':
       session.clear()
       flash('You are now logged out.', 'success')
   return redirect(url_for('index'))