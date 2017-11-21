from morphsvc.lib.engines.AlpheiosLegacyRemoteEngine import AlpheiosLegacyRemoteEngine

class AramorphLegacyRemoteEngine(AlpheiosLegacyRemoteEngine):


    def __init__(self,code, config,**kwargs):
       super(AramorphLegacyRemoteEngine, self).__init__(code, config,**kwargs)
       self.code = code
       self.language_codes = ['ara', 'ar']
       self.config = config
       self.uri = self.config['PARSERS_ARAMORPH_URI']
       self.rights = self.config['PARSERS_ARAMORPH_RIGHTS']
       self.remote_url = self.config['PARSERS_ARAMORPH_REMOTE_URL']
       self.transformer = None
