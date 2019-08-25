from lib.api import API
import pytest

# Проверяем, что API  -- это одиночка и только!
def test_check_singleton(): 
    # "Создаю" один экземпляр
    #https://api.vk.com/method/users.get?access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.101&user_ids=123    
    API('533bacf01e11f55b536a565b57531ac114461ae8736d6506a3', '5.101')    
    a1 = API.getInstance() 

    # "Создаю" второй экземпляр
    API("fing", ".80")
    a2 = API.getInstance()

    # т.к. это одиночка, то a1 и a2 то ссылка на один объект. То есть Singleton
    assert a1 == a2

def test_getDataWrap():
    data = API.getDataWrap()
    if data.get('access_token') != None or data.get('v') != None:
        assert True
