"""this is a translator module"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
#here we add apikey and url from ibm cloud
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    """ this func translates English to French """
    englishtranslation = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    return englishtranslation.get('translations')[0].get('translation')

def french_to_english(frenchtext):
    """ this func translates French to English """
    frenchtranslation = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    return frenchtranslation.get('translations')[0].get('translation')
    