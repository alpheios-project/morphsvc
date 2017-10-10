from lxml import etree
from json import dumps

from morphsvc.lib.xmljson import legacy as legacy

from morphsvc.lib.engines.engine import Engine
from  morphsvc.lib.transformers.OaLegacyTransformer import OaLegacyTransformer


class AlpheiosLegacyXmlEngine(Engine):

    def __init__(self, code, config,**kwargs):
        self.code = code
        self.uri = ""

    def get_uri(self):
        return self.uri

    def as_annotation(self, annotation_uri, word_uri,analysis):
        return analysis

    def output_json(self, engine_response):
        return dumps(legacy.data(engine_response),ensure_ascii=False)

    def output_xml(self, engine_response):
        return etree.tostring(engine_response, pretty_print=True, encoding='unicode')

    def to_cache(self, engine_response):
        return etree.tostring(engine_response, pretty_print=True, encoding='unicode')

    def from_cache(self,cached_response):
        return etree.fromstring(cached_response)
