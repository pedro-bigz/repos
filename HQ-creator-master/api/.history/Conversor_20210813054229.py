from Compressor import Compressor

class Conversor:
    def __init__(self, paths):
        self.compressor = None
        self.initOperation(paths)
    
    def initOperation(self, paths):
        try:
            self.setPaths(paths)
            self.compress()
            self.convertToCbr()
        except:
            self.rollback()
        
    def setPaths(self, paths):
        self.paths = paths
        
    def compress(self):
        self.compressor = Compressor(self.paths)
        
    def convertToCbr(self):
        self.compressor.toCbr()
        
    def rollback(self):
        self.compressor.rollback()