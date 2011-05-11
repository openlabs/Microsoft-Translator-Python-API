# -*- coding: utf-8 -*-
"""
    __init__

    A translator using the micrsoft translation engine documented here:

    http://msdn.microsoft.com/en-us/library/ff512419.aspx

    :copyright: © 2011 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

__all__ = ['Translator']

try:
    import simplejson as json
    from simplejson import JSONDecodeError
except ImportError:
    import json
    class JSONDecodeError(Exception): pass
    # Ugly: No alternative because this exception class doesnt seem to be there
    # in the standard python module
import urllib


class ArgumentOutOfRangeException(Exception): 
    def __init__(self, message):
        self.message = message.replace('ArgumentOutOfRangeException: ', '')
        super(ArgumentOutOfRangeException, self).__init__(self.message)


class TranslateApiException(Exception):
    def __init__(self, message):
        self.message = message.replace('TranslateApiException: ', '')
        super(TranslateApiException, self).__init__(self.message)


class Translator(object):
    """Implements AJAX API for the Microsoft Translator service

    :param app_id: A string containing the Bing AppID.
    """

    def __init__(self, app_id):
        """
        :param app_id: A string containing the Bing AppID.
        """
        self.app_id = app_id

    def call(self, url, params):
        """Calls the given url with the params urlencoded
        """
        params['appId'] = self.app_id
        response = urllib.urlopen(
            "%s?%s" % (url, urllib.urlencode(params))).read()
        rv =  json.loads(response.decode("UTF-8-sig"))

        if isinstance(rv, basestring) and \
                rv.startswith("ArgumentOutOfRangeException"):
            raise ArgumentOutOfRangeException(rv)

        if isinstance(rv, basestring) and \
                rv.startswith("TranslateApiException"):
            raise TranslateApiException(rv)

        return rv

    def translate(self, text, to_lang, from_lang=None, 
            content_type='text/plain', category='general'):
        """Translates a text string from one language to another.

        :param text: A string representing the text to translate.
        :param to_lang: A string representing the language code to 
            translate the text into.
        :param from_lang: A string representing the language code of the 
            translation text. If left None the response will include the 
            result of language auto-detection. (Default: None)
        :param content_type: The format of the text being translated. 
            The supported formats are "text/plain" and "text/html". Any HTML 
            needs to be well-formed.
        :param category: The category of the text to translate. The only 
            supported category is "general".
        """
        params = {
            'text': text,
            'to': to_lang,
            'contentType': content_type,
            'category': category,
            }
        if from_lang is not None:
            params['from'] = from_lang
        return self.call(
            "http://api.microsofttranslator.com/V2/Ajax.svc/Translate",
            params)

    def translate_array(self, texts, to_lang, from_lang=None, **options):
        """Translates an array of text strings from one language to another.

        :param texts: A list containing texts for translation.
        :param to_lang: A string representing the language code to 
            translate the text into.
        :param from_lang: A string representing the language code of the 
            translation text. If left None the response will include the 
            result of language auto-detection. (Default: None)
        :param options: A TranslateOptions element containing the values below. 
            They are all optional and default to the most common settings.

                Category: A string containing the category (domain) of the 
                    translation. Defaults to "general".
                ContentType: The format of the text being translated. The 
                    supported formats are "text/plain" and "text/html". Any 
                    HTML needs to be well-formed.
                Uri: A string containing the content location of this 
                    translation.
                User: A string used to track the originator of the submission.
                State: User state to help correlate request and response. The 
                    same contents will be returned in the response.
        """
        options = {
            'Category': "general",
            'Contenttype': "text/plain",
            'Uri': '',
            'User': 'default',
            'State': ''
            }.update(options)
        params = {
            'texts': json.dumps(texts),
            'to': to_lang,
            'options': json.dumps(options),
            }
        if from_lang is not None:
            params['from'] = from_lang

        return self.call(
                "http://api.microsofttranslator.com/V2/Ajax.svc/TranslateArray",
                params)
