class Path:
    def __init__(self, content):
        self.args = ""
        self.content = content
        
    def parseString(self):
        self.args = self.content.split("&")