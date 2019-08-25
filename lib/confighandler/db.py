'''
    Экземпляры сего класса при создании пишут в своё поле данные из объекта.
    Ссылка на объект собирается из аргуменьтов, принятых при создании
    экземпляра.
'''
class DB():
    def __init__(self,unitkind,source_convey_layer3):
        self.connection_string = source_convey_layer3[unitkind]['database']['connectionString']
