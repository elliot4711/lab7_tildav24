class DictHash:
    def __init__(self):
        self.dict = dict()

    def store(self, key, data):
        self.dict[key] = data

    def __contains__(self, key):
        if key in self.dict:
            return True
        else:
            return False

    def search(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return -1

    def __getitem__(self, key):
        return self.search(key)   