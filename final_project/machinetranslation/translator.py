import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#authenticate

authenticator = IAMAuthenticator(apikey)

#setup service
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

lt.set_service_url(url)


def englishToFrench(english_text):
    #write the code here
    french_text = lt.translate(text=english_text, model_id='en-fr').get_result()
    #getting the resulting translation
    return french_text

def frenchToEnglish(french_text):
    #write the code here
    english_text = lt.translate(text=french_text, model_id='fr-en').get_result()
    #getting the resulting translation
    return english_text
