from morphsvc.lib.engines.AlpheiosXmlEngine import AlpheiosXmlEngine
from subprocess import check_output
import itertools
from lxml import etree
from collections import Callable
import os, requests, re
from morphsvc.lib.transformers.BetacodeTransformer import BetacodeTransformer
from morphsvc.lib.transformers.LatinTransformer import LatinTransformer

class WhitakersLocalEngine(AlpheiosXmlEngine):
    """ Whitakers Local Engine (Whitakers is callable locally)
    """

    def __init__(self,code, config,**kwargs):
       """ Constructor
       :param code: code
       :type code: str
       :param config: app config
       :type config: dict
       """
       super(WhitakersLocalEngine, self).__init__(code, config,**kwargs)
       self.code = code
       self.config = config
       self.language_codes = ['la', 'lat' ]
       self.uri = self.config['PARSERS_WHITAKERS_URI']
       self.wordsxml_path = self.config['PARSERS_WHITAKERS_PATH']
       self.latin_transformer = LatinTransformer(config)

    def lookup(self,word=None,word_uri=None,language=None,request_args=None,**kwargs):
        """ Word Lookup Function
        :param word: the word to lookup
        :type word: str
        :param word_uri: a uri for the word
        :type word_uri: str
        :param language: the language code for the word
        :type language: str
        :param request_args: dict of engine specific request arguments
        :type request_args: dict
        :return: the analysis
        :rtype: str
        """
        word = self.latin_transformer.transform_input(word)
        parsed = self._execute_query(word)
        if not isinstance(parsed,str):
            parsed = parsed.decode('utf-8')
        # this is a ridiculous hack to preserve backwards consistency - the old
        # Alpheios mod_perl wrapper stripped the # sign off the hdwds
        parsed = re.sub(r'#(\d+)</hdwd>', '\\1</hdwd>', parsed)
        transformed = etree.fromstring(parsed)
        return transformed

    def _execute_query(self,word):
        """ Spawns a local process to execute wordsxml and return the output
        :param word: word to analyze
        :type worD: str
        :return: output
        :rtype: str
        """
        cwd = re.sub(r'/wordsxml$','',self.wordsxml_path)
        return check_output(itertools.chain([self.wordsxml_path],[],[word]),cwd=cwd)

    def options(self):
        """ get the engine specific request arguments
        :return: engine specific request arguments or None if there aren't any
        :rtype: dict
        """
        return {}
