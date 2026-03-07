from flask import render_template, Blueprint
from blog.models import Post

bp = Blueprint("main", __name__)

@bp.route("/")
def homepage():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)
    