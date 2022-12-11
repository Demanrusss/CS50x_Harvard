from aifc import Error
import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'TRANSLATOR_KEY' not in app.config or not app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured')
    auth = {'DeepL-Auth-Key': app.config['TRANSLATOR_KEY']}
    request = requests.get('https://api-free.deepl.com/v2'
        '/translate?text={}&source_lang={}'
        '&target_lang={}'.format(text, source_language, dest_language),
        headers = auth)
    if request.status_code != 200:
        return _('Error: the translation service failed')
    return json.loads(request.content.decode('utf-8-sig'))
