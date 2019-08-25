'''
    Экземпляры сего класса при создании пишут в свои поля данные из объекта.
    Ссылка на объект собирается из аргуменьтов, принятых при создании
    экземпляра.
'''
class VK_API():
    def __init__(self,unitkind,source_convey_layer3):
        self.token=source_convey_layer3[unitkind]['vkapi']['token']
        self.secret_key=source_convey_layer3[unitkind]['vkapi']['secret-key']
        self.auth_token=source_convey_layer3[unitkind]['vkapi']['auth-token']
        self.group_id=source_convey_layer3[unitkind]['vkapi']['group-id']