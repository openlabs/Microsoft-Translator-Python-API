# -*- coding: utf-8 -*-
"""
    test

    Test the translator

    :copyright: (c) 2012 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import os
import unittest
from microsofttranslator import Translator, TranslateApiException

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

default_languages = [u'en', u'fr', u'de']


class TestTranslator(unittest.TestCase):

    def test_translate(self):
        client = Translator(client_id, client_secret, debug=True)
        self.assertEqual(
            client.translate("hello", "pt"), u'Ol\xe1'
        )

    def test_translate_array(self):
        client = Translator(client_id, client_secret, debug=True)
        self.assertEqual(client.translate("hello", "pt"), u'Ol\xe1')

    def test_invalid_client_id(self):
        client = Translator("foo", "bar")
        with self.assertRaises(TranslateApiException):
            client.translate("hello", "pt")

    def test_get_languages(self):
        client = Translator(client_id, client_secret, debug=True)
        languages = client.get_languages()
        self.assertEqual(type(languages), list)
        self.assertTrue(set(default_languages).issubset(set(languages)))

    def test_detect_language(self):
        client = Translator(client_id, client_secret, debug=True)
        self.assertEqual(client.detect_language('hello'), u'en')


def test_all():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestTranslator))
    return suite


if __name__ == '__main__':
    unittest.main()
