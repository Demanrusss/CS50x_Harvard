from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _babel
from elasticsearch import Elasticsearch

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = _babel('To view this page, please, log in first')
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
    if app.config['ELASTICSEARCH_URL'] else None

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(mailhost = (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                                   fromaddr = 'no-reply@' + app.config['MAIL_SERVER'],
                                   toaddrs = app.config['ADMINS'],
                                   subject = 'Blog failure',
                                   credentials = auth,
                                   secure = secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/blog.log', maxBytes = 10240, backupCount = 10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Blog startup')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app import routes, models, errors

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
# In order to test mail.server by python                            #
#                                                                   #
# $ python -m smtpd -n -c DebuggingServer localhost:8025            #
# $ export/set(for windows) MAIL_SERVER=localhost                   #
# $ export/set(for windows) MAIL_PORT=8025                          #
#                                                                   #
# OR                                                                #
#                                                                   #
# $ export/set(for windows) MAIL_SERVER=smtp.googlemail.com         #
# $ export/set(for windows) MAIL_PORT=587                           #
# $ export/set(for windows) MAIL_USE_TLS=1                          #
# $ export/set(for windows) MAIL_USERNAME=<gmail-username>          #
# $ export/set(for windows) MAIL_PASSWORD=<gmail-password>          #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
# In terms of using flask-babel here are some useful commands:      #
#                                                                   #
# Extracting every message for translation (and updating)           #
# $ pybabel extract -F babel.cfg -k _babel -o messages.pot .        #
# $ pybabel update -i messages.pot -d app/translations              #
#                                                                   #
# Creating a file for every needed language                         #
# $ pybabel init -i messages.pot -d app/translations -l ru          #
#   creating catalog app/translations/ru/LC_MESSAGES/messages.po    #
#   based on messages.pot                                           #
#                                                                   #
# Compiling translation to the application                          #
# $ pybabel compile -d app/translations                             #
#   compiling catalog app/translations/ru/LC_MESSAGES/messages.po   #
#   to app/translations/ru/LC_MESSAGES/messages.mo                  #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #