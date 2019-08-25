class Dict(dict):
    def __init__(self):
        self= dict()

    def add(self, key, value):
            self[key] = value

    def add_dict(self, d: dict()):
        for key, value in d.items():
            self.add(key, value)