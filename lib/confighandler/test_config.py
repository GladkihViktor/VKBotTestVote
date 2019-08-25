from .config import config
from .config import readconfig
import pytest
import json

'''You can start it with typing: pytest -v -s'''

configcontent=None
def setup_module(module):
    global configcontent
    configcontent=json.load(open("config.json", mode='r'))


@pytest.mark.parametrize('recordkind, block, attribute, result', 
                         [
                             ('softwareversion', '', '', '1.0.0'),
                             ('fileversion', '', '', '1.0.0'),
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

def test_config(recordkind, block, attribute, result):
    config_inst=config(configcontent)
    if recordkind == 'softwareversion' or recordkind == 'fileversion':
        assert getattr(config_inst, recordkind) == result
    else: 
        assert getattr(getattr(getattr(config_inst, recordkind), block), attribute) == result


@pytest.mark.parametrize('recordkind, block, attribute, result', 
                         [
                             ('softwareversion', '', '', '1.0.0'),
                             ('fileversion', '', '', '1.0.0'),
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

def test_readconfig(recordkind, block, attribute, result):
    config_inst=readconfig()
    if recordkind == 'softwareversion' or recordkind == 'fileversion':
        assert getattr(config_inst, recordkind) == result
    else: 
        assert getattr(getattr(getattr(config_inst, recordkind), block), attribute) == result

    