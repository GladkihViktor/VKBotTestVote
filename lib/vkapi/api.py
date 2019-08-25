class API():    
        # Одиночка. Экземпляр
    __instance = None

    # access_token=""
    # v=""

    #   https://api.vk.com/method/messages.send?
    url ="https://api.vk.com"
    
    def __init__(self, access_token:str, v:str): 
        # если объект не создан, создадим. 
        if API.__instance == None:
            self.access_token= access_token
            self.v = v
            API.__instance = self
            
    @staticmethod # Статичный метод
    def getInstance(): 
        if API.__instance != None:            
            return API.__instance 
        raise Exception("This class is a singleton! Please init instance!")

    @staticmethod
    def getDataWrap():
        return {                
                'access_token': API.getInstance().access_token, 
                'v': API.getInstance().v
            }
            
