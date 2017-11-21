from morphsvc.lib.engines.AlpheiosRemoteEngine import AlpheiosRemoteEngine
from morphsvc.lib.transformers.BuckwalterTransformer import BuckwalterTransformer

class AramorphRemoteEngine(AlpheiosRemoteEngine):


    def __init__(self,code, config,**kwargs):
       super(AramorphRemoteEngine, self).__init__(code, config,**kwargs)
       self.code = code
       self.language_codes = ['ara', 'ar']
       self.config = config
       self.uri = self.config['PARSERS_ARAMORPH_URI']
       self.rights = self.config['PARSERS_ARAMORPH_RIGHTS']
       self.remote_url = self.config['PARSERS_ARAMORPH_REMOTE_URL']
       self.transformer = BuckwalterTransformer(config)
