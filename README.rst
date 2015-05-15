Microsoft Translator V2 -- Python API
=====================================

:Version: 0.7
:Web: http://openlabs.co.in/
:keywords: Microsoft Translator
:copyright: Openlabs Technologies & Consulting (P) LTD
:license: BSD

.. image:: https://secure.travis-ci.org/openlabs/Microsoft-Translator-Python-API.png?branch=master
   :target: http://travis-ci.org/#!/openlabs/Microsoft-Translator-Python-API

.. image:: https://coveralls.io/repos/openlabs/Microsoft-Translator-Python-API/badge.png?branch=master
  :target: https://coveralls.io/r/openlabs/Microsoft-Translator-Python-API


This python API implements the Microsoft Translator services which can be used 
in web or client applications to perform language translation operations. The 
services support users who are not familiar with the default language of a page 
or application, or those desiring to communicate with people of a different 
language group.


Example Usage:
::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Client ID>', '<Your Client Secret>')
        >>> print translator.translate("Hello", "pt")
        "Olá"

Registering your application
----------------------------

To register your application with Azure DataMarket, 
visit https://datamarket.azure.com/developer/applications/ using the
LiveID credentials from step 1, and click on “Register”. In the
“Register your application” dialog box, you can define your own
Client ID and Name. The redirect URI is not used for the Microsoft
Translator API. However, the redirect URI field is a mandatory field,
and you must provide a URI to obtain the access code. A description is
optional.

Take a note of the client ID and the client secret value.

Features
--------

Translation
+++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Client ID>', '<Your Client Secret>')
        >>> print translator.translate("Hello", "pt")
        "Olá"

Translate multiple words at once
++++++++++++++++++++++++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Client ID>', '<Your Client Secret>')
        >>> translator.translate_array(['apple', 'orange'], 'pt')
        [{u'TranslatedText': u'Apple', u'From': u'en', u'OriginalTextSentenceLengths': [5], u'TranslatedTextSentenceLengths': [5]}, {u'TranslatedText': u'laranja', u'From': u'en', u'OriginalTextSentenceLengths': [6], u'TranslatedTextSentenceLengths': [7]}]

Get supported languages
+++++++++++++++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Client ID>', '<Your Client Secret>')
        >>> print translator.get_languages()
        [u'ar', u'bg', u'ca', u'zh-CHS', u'zh-CHT', u'cs', u'da', u'nl', u'en', u'et', u'fi', u'fr', u'de', u'el', u'ht', u'he', u'hi', u'mww', u'hu', u'id', u'it', u'ja', u'tlh', u'tlh-Qaak', u'ko', u'lv', u'lt', u'ms', u'mt', u'no', u'fa', u'pl', u'pt', u'ro', u'ru', u'sk', u'sl', u'es', u'sv', u'th', u'tr', u'uk', u'ur', u'vi', u'cy']

Detect Language
+++++++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Client ID>', '<Your Client Secret>')
        >>> translator.detect_language('hello')
        u'en'


Bugs and Development on Github
------------------------------

https://github.com/openlabs/Microsoft-Translator-Python-API
