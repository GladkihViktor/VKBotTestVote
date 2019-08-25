from .Unit import unit
import pytest
import json

'''You can start it with typing: pytest -v -s'''

configcontent=None
def setup_module(module):
    global configcontent
    configcontent=json.load(open("config.json", mode='r'))

@pytest.mark.parametrize('recordkind, block, attribute, result', 
                         [
                             ('Production', 'vkapi', 'token', '1'),
                             ('Production', 'vkapi', 'secret_key', '2'),
                             ('Production', 'vkapi', 'auth_token', '3'),
                             ('Production', 'vkapi', 'group_id', '4'),
                             ('Production', 'db', 'connection_string', '5'),
                             ('Develop', 'vkapi', 'token', '6'),
                             ('Develop', 'vkapi', 'secret_key', '7'),
                             ('Develop', 'vkapi', 'auth_token', '8'),
                             ('Develop', 'vkapi', 'group_id', '9'),
                             ('Develop', 'db', 'connection_string', '10'),
                         ]
                         )
def test_unit(recordkind, block, attribute, result):
    unit_inst=unit(recordkind,configcontent)
    assert getattr(getattr(unit_inst, block), attribute) == result