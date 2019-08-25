from .vkapi import VK_API
import pytest
import json

'''You can start it with typing: pytest -v -s'''

configcontent=None
def setup_module(module):
    global configcontent
    configcontent=json.load(open("config.json", mode='r'))

@pytest.mark.parametrize('recordkind, attribute, result', 
                         [
                             ('Develop', 'token', '6'),
                             ('Develop', 'secret_key', '7'),
                             ('Develop', 'auth_token', '8'),
                             ('Develop', 'group_id', '9'),
                             ('Production', 'token', '1'),
                             ('Production', 'secret_key', '2'),
                             ('Production', 'auth_token', '3'),
                             ('Production', 'group_id', '4')
                         ]
                         )
def test_vkapi(recordkind, attribute, result):
    vkapi_inst=VK_API(recordkind,configcontent)
    assert getattr(vkapi_inst, attribute) == result