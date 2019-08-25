'''
    Экземпляр сего класса при создании создаёт два класса низшего уровня
    и пишет их себе в поля. Принимая аргументы при инициации он передает их
    низшим классам при их создании.
'''
from .vkapi import VK_API
from .db import DB

class unit():
    """This class unites in its attributes instancies of the classes VK_API and DB. 
    These classes are provided with argument(unitkind) in order to distinguish develop/production records"""
    def __init__(self,unitkind,source_convey_layer2):
       self.vkapi = VK_API(unitkind,source_convey_layer2)
       self.db = DB(unitkind, source_convey_layer2)

