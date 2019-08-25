import pytest
from lib.api import API
from lib.handlers import APIHandler


def test_initURL():
    # Должны получить:
    #https://api.vk.com/method/users.get?access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.101&user_ids=123
    true_str = 'https://api.vk.com/method/users.get?access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.101&user_ids=123'    
    handle = APIHandler()
    str_handle =  handle.initURL('users.get', {"user_ids": 123})    
    assert  str_handle == true_str

def test_execute():
    # Пока что контролируем, что мы из метода получим число, то есть номер статуса запроса!
    handle = APIHandler()
    result = handle.execute('users.get', {"user_ids": 123})        
    assert type(result).__name__ == 'int'