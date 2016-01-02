class Voter(object):
    #TODO
    '''
        Simple aggregation of multiple classifiers
        The base classifiers are the same model but different hyperparameters
    '''

    def __init__(self, classifier, k=10):
        # classifier should be imported from pyml.supervised
        self.classifier = classifier
        self.k = k

    def fit(self, data, target):
        pass
        

