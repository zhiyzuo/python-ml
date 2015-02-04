import helpers
class Feature:
#TODO
    def __init__(self, data):
    # data should be in the form of list or numpy array
        self.features = data
        self.dimension = len(data[0])
        self.size = len(data)
    def getDimension(self):
        return self.dimension
    def getFeatures(self):
        return self.features
    def normalize(self, method="linear", columns=None):
        if columns == None:
            columns = range(0, self.dimension)
        for col in columns:
            # extract a specified column from feature space
            feature = [[sample[col]] for sample in self.features]
            feature = helpers.normalize(feature, method)
