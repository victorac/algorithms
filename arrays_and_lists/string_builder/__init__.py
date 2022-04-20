class StringBuilder:
    def __init__(self):
        self.string = []

    def append(self, word:str):
        self.string.extend(word)
    
    def to_string(self):
        return "".join(self.string)


