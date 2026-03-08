import os

basedir = os.path.abspath(os.path.dirname(__file__))

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "change-me")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "blog.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"
#note to future self remove password from config.py    