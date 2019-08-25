from .api import API
from urllib.parse import urlencode
from core.dict import Dict
import requests as request_to

class APIHandler():

    def __init__(self): 
        self.api = API.getInstance()

    def initURL(self, method_name: str, params:dict()):
        body = Dict()
        body.add_dict(self.api.getDataWrap())    
        body.add_dict(params)            
        
        body_url= self.api.url + '/method/'+method_name+'?' + urlencode(body)
        return  body_url

    def execute(self, method_name: str, params:{}):        
        url = self.initURL(method_name, params)
        request = request_to.get(url)
        return request.status_code #200 or #404 or etc...