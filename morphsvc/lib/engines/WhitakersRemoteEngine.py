from morphsvc.lib.engines.AlpheiosRemoteEngine import AlpheiosRemoteEngine

class WhitakersRemoteEngine(AlpheiosRemoteEngine):


    def __init__(self,code,config,**kwargs):
       super(WhitakersRemoteEngine, self).__init__(code, config,**kwargs)
       self.code = code
       self.config = config
       self.uri = self.config['PARSERS_WHITAKERS_URI']
       self.remote_url = self.config['PARSERS_WHITAKERS_REMOTE_URL']
       self.rights = self.config['PARSERS_WHITAKERS_RIGHTS']
       self.language_codes = ['lat','la']
