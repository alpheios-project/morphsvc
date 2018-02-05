from lxml import etree
from json import dumps
from hazm.Stemmer import Stemmer
from hazm.Lemmatizer import Lemmatizer
from hazm.Normalizer import Normalizer
from datetime import datetime
import os

from morphsvc.lib.xmljson import legacy as legacy

from morphsvc.lib.engines.AlpheiosXmlEngine import AlpheiosXmlEngine
from  morphsvc.lib.transformers.OaLegacyTransformer import OaLegacyTransformer


class HazmEngine(AlpheiosXmlEngine):

    def __init__(self,code, config,**kwargs):
        """ Constructor
        :param code: code
        :type code: str
        :param config: app config
        :type config: dict
        """
        super(HazmEngine, self).__init__(code, config,**kwargs)
        self.code = code
        self.config = config
        self.code = code
        self.oa_transformer = OaLegacyTransformer()
        self.language_codes = ['per','fas']
        self.uri = self.config['PARSERS_HAZM_URI']
        self.rights = self.config['PARSERS_HAZM_RIGHTS']
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()

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
        normalizer = Normalizer()
        item = normalizer.normalize(word)
        analyses = []
        wordstem = self.stemmer.stem(item)
        lemma = self.lemmatizer.lemmatize(item)
        #wordtagged = self.tagger.tag(word_tokenize(item))
        #wordpofs = wordtagged[0][1]
        #wordpofs = self.maptohazm(wordpofs)
        analysis = {}
        analysis['entries'] = []
        entry = {}
        entry['dict'] = {}
        entry['dict']['hdwd'] = {}
        entry['dict']['hdwd']['lang'] = 'per'
        entry['dict']['hdwd']['text'] = lemma
        entry['infls'] = []
        infl = {}
        infl['stem'] = {}
        infl['stem']['text'] = wordstem
        infl['stem']['lang'] = 'per'
        infl['pofs'] = {}
        #if wordpofs:
        #    infl['pofs']['order'] = str(wordpofs[1])
        #    infl['pofs']['text'] = wordpofs[0]
        entry['infls'].append(infl)
        analysis['entries'].append(entry)
        analyses.append(analysis)
        return self.toalpheiosxml(analyses)

    def maptohazm(self,wordpofs):
        mapped = None
        if wordpofs == "N":
            mapped = ["noun", 1]
        elif wordpofs == "INT":
            mapped = ["interjection", 2]
        elif wordpofs == "DET":
            mapped = ["determiner", 3]
        elif wordpofs == "AJ":
            mapped = ["adjective", 4]
        elif wordpofs == "P":
            mapped = ["preposition", 5]
        elif wordpofs == "PRO":
            mapped = ["pronoun", 6]
        elif wordpofs == "CONJ":
            mapped = ["conjunction", 7]
        elif wordpofs == "V":
            mapped = ["verb", 8]
        elif wordpofs == "ADV":
            mapped = ["adverb", 9]
        elif wordpofs == "POSTP":
            mapped = ["postposition", 10]
        elif wordpofs == "Num":
            mapped = ["numeral", 11]
        elif wordpofs == "CL":
            mapped = ["classifier", 12]
        elif wordpofs == "e":
            mapped = ["ezafe", 13]
        return mapped


    def toalpheiosxml(self,analysis):
        '''
        represents an analysis in alpheios  xml format
        '''
        root = etree.Element('entries')
        for item in analysis:
            for entry in item['entries']:
                root.append(self.entrytoxml(entry))
        return root


    def entrytoxml(self,entry):
        '''
        represents an entry from an analysis in an xml fragment per the alpheios schema
        '''
        root = etree.Element('entry')
        dic = etree.SubElement(root, 'dict')
        hdwd = etree.SubElement(dic, 'hdwd',
                                {'{http://www.w3.org/XML/1998/namespace}lang': entry['dict']['hdwd']['lang']})
        hdwd.text = entry['dict']['hdwd']['text']
        for i in entry['infls']:
            infl = etree.SubElement(root, 'infl')
            term = etree.SubElement(infl, 'term', {'{http://www.w3.org/XML/1998/namespace}lang': i['stem']['lang']})
            stem = etree.SubElement(term, 'stem')
            stem.text = i['stem']['text']
            if (i['pofs'] and i['pofs']['text']):
                pofs = etree.SubElement(infl, 'pofs', {'order': i['pofs']['order']})
                pofs.text = i['pofs']['text']
        return root
