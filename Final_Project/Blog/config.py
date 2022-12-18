import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 5
    #For sending a notification about errors
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['deman.russs@gmail.com']
    LANGUAGES = ['en', 'es', 'ru']
    # --> Google, Microsoft Translate through RapidAPI.com
    TRANSLATOR_KEY = os.environ.get('TRANSLATOR_KEY') or \
        '9bc694957dmsh9021abeb4375ec0p150998jsnef4cde8cffb6'
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') or \
        'http://localhost:9200'