import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'TRANSLATOR_KEY' not in app.config or not app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured')
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = 'source={}&target={}&q={}'.format(source_language, dest_language, text)
    headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "Accept-Encoding": "application/gzip",
	    "X-RapidAPI-Key": "{}".format(app.config['TRANSLATOR_KEY']),
	    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data = payload, headers = headers)
    if response.status_code != 200:
        url = "https://microsoft-translator-text.p.rapidapi.com/translate"
        querystring = {"api-version":"3.0",
                       "to[0]":"{}".format(dest_language),
                       "textType":"plain",
                       "profanityAction":"NoAction"}
        payload = [{"Text": "{}".format(text)}]
        headers = {
	        "content-type": "application/json",
	        "X-RapidAPI-Key": "9bc694957dmsh9021abeb4375ec0p150998jsnef4cde8cffb6",
	        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
        }
        response = requests.request("POST", url, json = payload, headers = headers, params = querystring)
        if response.status_code != 200:
            return _('Error: the translation service failed') + \
                '. Status code: {}'.format(response.status_code)
        r = json.loads(response.text)
        return r[0]["translations"][0]["text"]
    return response.text
    
