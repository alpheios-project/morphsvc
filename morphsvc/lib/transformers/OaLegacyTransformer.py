import pkg_resources
from lxml import etree
from datetime import datetime

class OaLegacyTransformer:

   def  __init__(self, *args,**kwargs):
      resource_package = __name__
      xslt_path = '/' .join(('xslt','wrap_oa_legacy.xsl'))
      xslt = pkg_resources.resource_string(resource_package,xslt_path)
      self.xslt_transformer = etree.XSLT(etree.XML(xslt))

   def wrap(self, annotation_uri, word_uri, engine_uri, xml, engine_rights):
      annotation_uri_param = etree.XSLT.strparam(annotation_uri)
      word_uri_param = etree.XSLT.strparam(word_uri)
      engine_uri_param = etree.XSLT.strparam(engine_uri)
      engine_rights_param = etree.XSLT.strparam(engine_rights)
      createdat_param = etree.XSLT.strparam(datetime.utcnow().isoformat())
      transformed = self.xslt_transformer(xml,e_annotationuri = annotation_uri_param,
                                          e_worduri = word_uri_param,
                                          e_datetime = createdat_param,
                                          e_agenturi = engine_uri_param,
                                          e_agentrights= engine_rights_param)
      return etree.fromstring(etree.tostring(transformed,encoding="unicode"))
