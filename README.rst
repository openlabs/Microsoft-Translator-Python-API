Microsoft Translator V2 -- Python API
=====================================

:Version: 0.1 
:Web: http://openlabs.co.in/
:keywords: Micrsoft Translator

This python API implements the Microsoft Translator services which can be used 
in web or client applications to perform language translation operations. The 
services support users who are not familiar with the default language of a page 
or application, or those desiring to communicate with people of a different 
language group.


Example Usage:
::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your API Key>')
        >>> print translator.translate("Hello", "pt")
        "Olá"


