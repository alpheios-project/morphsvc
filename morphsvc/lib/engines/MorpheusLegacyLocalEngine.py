from morphsvc.lib.engines.AlpheiosLegacyXmlEngine import AlpheiosLegacyXmlEngine
from subprocess import check_output
import itertools
from lxml import etree
from collections import Callable
from morphsvc.lib.transformers.AsciiGreekTransformer import AsciiGreekTransformer
import os, requests, re

class MorpheusLegacyLocalEngine(AlpheiosLegacyXmlEngine):
    """ Morpheus Legacy Local Engine (Morpheus is callable locally)
    """

    def __init__(self,code, config,**kwargs):
       """ Constructor
       :param code: code
       :type code: str
       :param config: app config
       :type config: dict
       """
       super(MorpheusLegacyLocalEngine, self).__init__(code, config,**kwargs)
       self.code = code
       self.config = config
       self.language_codes = ['grc']
       self.uri = self.config['PARSERS_MORPHEUS_URI']
       self.rights = self.config['PARSERS_MORPHEUS_RIGHTS']
       self.morpheus_path = self.config['PARSERS_MORPHEUS_PATH']
       self.transformer = AsciiGreekTransformer(config)

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
        args = self.make_args(language,request_args)
        word = self.transformer.transform_input(word)
        parsed = self._execute_query(args,word)
        # this is a ridiculous hack to preserve backwards consistency - the old
        # Alpheios mod_perl wrapper stripped the # sign off the hdwds
        if not isinstance(parsed,str):
            parsed = parsed.decode('utf-8')
        parsed = re.sub(r'#(\d+)</hdwd>', '\\1</hdwd>', parsed)
        return etree.fromstring(parsed)

    def _execute_query(self,args,word):
        """ Spawns a local process to execute morpheus and return the output
        :param args: request argments
        :type args: list
        :param word: word to analyze
        :type worD: str
        :return: output
        :rtype: str
        """
        return check_output(itertools.chain([self.morpheus_path], args, [word]))

    def make_args(self,lang,request_args):
        args = []
        args.append("-m"+self.config['PARSERS_MORPHEUS_STEMLIBDIR'])
        if 'strictCase' in request_args and request_args['strictCase'] == '1':
            pass
        else:
            # default behavior is case insensitive match
            args.append('-S')
        if 'checkPreverbs' in request_args and request_args['checkPreverbs'] == '1':
            args.append('-c')
        return args

    def options(self):
        """ get the engine specific request arguments
        :return: engine specific request arguments or None if there aren't any
        :rtype: dict
        """
        return {'strictCase': '^1$','checkPreverbs':'^1$'}
