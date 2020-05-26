import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    headers = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Content-type': 'application/json'
    }
    body = [{
        'text': '%s' % text
    }]
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(source_language, dest_language),
        headers=headers,
        json=body)
    print("%s" % r)
    if r.status_code != 200:
        return r.content.decode('utf-8-sig')
    return json.loads(r.content.decode('utf-8-sig'))