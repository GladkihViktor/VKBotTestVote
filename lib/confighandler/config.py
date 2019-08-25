'''
    Экземпляр сего класса при создании создаёт два класса среднего уровня
    и пишет их себе в поля. Принимая аргумент при инициации он передает его
    средним классам при их создании.
'''
import json
from .Unit import unit

class config():
    def __init__(self, source_convey_layer1):    
        self.softwareversion = '1.0.0'
        self.fileversion=source_convey_layer1['version']
        self.Develop = unit("Develop", source_convey_layer1)
        self.Production = unit("Production", source_convey_layer1) 

def readconfig(pathtoconfig='config.json'):
    configfile=open(pathtoconfig, mode='r')
    configcontent=json.load(configfile)
    configfile.close()
    conf = config(configcontent)
    return conf