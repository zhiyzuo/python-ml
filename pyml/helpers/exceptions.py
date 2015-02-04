class DimensionError(Exception):
    def __init__(self, object1, object2):
        self.msg = "Dimension of {} and {} mismatch!".format(object1, object2)
    def __str__(self):
        return repr(self.msg)
        
