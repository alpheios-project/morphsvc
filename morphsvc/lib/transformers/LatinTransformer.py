import pkg_resources
from lxml import etree
import requests, html, re

class LatinTransformer:

   def  __init__(self, config, *args,**kwargs):
      pass

   def transform_input(self,input):
      input = re.sub(r'[^\w\d\s]', '', input)
      input = re.sub(r'[\u00c0\u00c1\u00c2\u00c3\u00c4\u0100\u0102]','A', input)
      input = re.sub(r'[\u00c8\u00c9\u00ca\u00cb\u0112\u0114]','E', input)
      input = re.sub(r'[\u00cc\u00cd\u00ce\u00cf\u012a\u012c]', 'I', input)
      input = re.sub(r'[\u00d2\u00d3\u00d4\u00df\u00d6\u014c\u014e]', 'O', input)
      input = re.sub(r'[\u00d9\u00da\u00db\u00dc\u016a\u016c]', 'U', input)
      input = re.sub(r'[\u00c6\u01e2]', 'AE', input)
      input = re.sub(r'[\u0152]', 'OE', input)
      input = re.sub(r'[\u00e0\u00e1\u00e2\u00e3\u00e4\u0101\u0103]', 'a', input)
      input = re.sub(r'[\u00e8\u00e9\u00ea\u00eb\u0113\u0115]', 'e', input)
      input = re.sub(r'[\u00ec\u00ed\u00ee\u00ef\u012b\u012d\u0129]', 'i', input)
      input = re.sub(r'[\u00f2\u00f3\u00f4\u00f5\u00f6\u014d\u014f]', 'o', input)
      input = re.sub(r'[\u00f9\u00fa\u00fb\u00fc\u016b\u016d]', 'u', input)
      input = re.sub(r'[\u00e6\u01e3]','ae', input)
      input = re.sub(r'[\u0153]', 'oe', input)
      return input


   def transform_output(self,output):
      return output
