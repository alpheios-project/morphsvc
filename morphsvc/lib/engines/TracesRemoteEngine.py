from morphsvc.lib.engines.AlpheiosRemoteEngine import AlpheiosRemoteEngine

class TracesRemoteEngine(AlpheiosRemoteEngine):


    def __init__(self,code,config,**kwargs):
       super(TracesRemoteEngine, self).__init__(code, config,**kwargs)
       self.code = code
       self.config = config
       self.uri = self.config['PARSERS_TRACES_URI']
       self.remote_url = self.config['PARSERS_TRACES_REMOTE_URL']
       self.rights = self.config['PARSERS_TRACES_RIGHTS']
       self.language_codes = ['gez']
