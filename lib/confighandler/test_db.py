from .db import DB
import pytest
import json

'''You can start it with typing: pytest -v -s'''

configcontent=None
def setup_module(module):
    global configcontent
    configcontent=json.load(open("config.json", mode='r'))

@pytest.mark.parametrize('recordkind, result', 
                         [
                             ('Develop', '10'),
                             ('Production', '5')
                         ]
                         )
def test_db(recordkind, result):
    db_inst=DB(recordkind,configcontent)
    assert db_inst.connection_string == result


