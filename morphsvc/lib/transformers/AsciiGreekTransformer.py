import pkg_resources
import re

class AsciiGreekTransformer:
    """
    Mirrors legacy transformation of Ascii Greek input in Alpheios mod_perl wrapper
    """

    def  __init__(self, config, *args,**kwargs):
        resource_package = __name__

    def transform_input(self,input):
        transformed = re.sub(r'\\','\\\\',input)
        transformed = re.sub('[\.,]','',transformed)
        transformed = '"' + transformed + '"'
        return transformed

    def transform_output(self,output):
        return output
