import numpy as np
import milk


features = np.random.rand(100,10) # 2d array of features: 100 examples of 10 features each
labels = np.zeros(100)

def nfoldcrossvalidate(features, labels):
    features[50:] += .5
    labels[50:] = 1
    confusion_matrix, names = milk.nfoldcrossvalidation(features, labels)
    print 'Accuracy:', confusion_matrix.trace()/float(confusion_matrix.sum())

def classifier(features=None, labels=None, train=False, data=None):
    if train:
        learner = milk.defaultclassifier()
        model = learner.train(features, labels)
    else:
        assert data
        assert model
        print model.apply(data)
