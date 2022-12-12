import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    #For sending a notification about errors
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['deman.russs@gmail.com']
    LANGUAGES = ['en', 'ru', 'es']
    TRANSLATOR_KEY = os.environ.get('TRANSLATOR_KEY')
    # TRANSLATOR_KEY = os.environ.get('cb7fa33a-eeb1-52a4-c914-c2cf6a260e95:fx') --> Deepl.com
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')