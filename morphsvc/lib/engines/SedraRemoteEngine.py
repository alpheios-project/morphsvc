from morphsvc.lib.engines.AlpheiosRemoteEngine import AlpheiosRemoteEngine
import requests

class SedraRemoteEngine(AlpheiosRemoteEngine):


    def __init__(self,code,config,**kwargs):
       super(SedraRemoteEngine, self).__init__(code, config,**kwargs)
       self.code = code
       self.config = config
       self.uri = self.config['PARSERS_SEDRA_URI']
       self.remote_url = self.config['PARSERS_SEDRA_REMOTE_URL']
       self.rights = self.config['PARSERS_SEDRA_RIGHTS']
       self.language_codes = ['syr']

    def _execute_query(self,word,language):
        url = self.remote_url + word + ".alpheios"
        # TODO this should come from config
        headers = {
          'User-Agent': 'AlpheiosMorphService-1.0',
        }
        response = requests.get(url,headers=headers)
        # TODO should really raise error
        #response.raise_for_status()
        return response.text
