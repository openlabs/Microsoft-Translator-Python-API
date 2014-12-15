# -*- coding: utf-8 -*-
"""
    test

    Test the translator

    :copyright: (c) 2012 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest
from microsofttranslator import Translator, TranslateApiException

client_id = "translaterpythonapi"
client_secret = "FLghnwW4LJmNgEG+EZkL8uE+wb7+6tkOS8eejHg3AaI="


class TestTranslator(unittest.TestCase):

    def test_translate(self):
        client = Translator(client_id, client_secret, debug=True)
        self.assertEqual(client.translate("hello", "pt"), u'Ol\xe1')

    def test_invalid_client_id(self):
        client = Translator("foo", "bar")
        with self.assertRaises(TranslateApiException):
            client.translate("hello", "pt")

    def test_get_languages(self):
        languages = [u'ar', u'bg', u'ca', u'zh-CHS', u'zh-CHT', u'cs', u'da',
         u'nl', u'en', u'et', u'fi', u'fr', u'de', u'el', u'ht', u'he', u'hi',
         u'mww', u'hu', u'id', u'it', u'ja', u'tlh', u'tlh-Qaak', u'ko', u'lv',
         u'lt', u'ms', u'mt', u'no', u'fa', u'pl', u'pt', u'ro', u'ru', u'sk',
         u'sl', u'es', u'sv', u'th', u'tr', u'uk', u'ur', u'vi', u'cy']
        client = Translator(client_id, client_secret, debug=True)
        self.assertEqual(client.get_languages(), languages)

    def test_detect_language(self):
        client = Translator(client_id, client_secret, debug=True)
        self.assertEqual(client.detect_language('hello'), 'en')


def test_all():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestTranslator))
    return suite


if __name__ == '__main__':
    unittest.main()
