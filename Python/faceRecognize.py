#Importing necessary packages
from time import time
import matplotlib.pyplot as plt
import numpy as np
from time import time
from cPickle import pickle

#importing machine learning packages
from sklearn.datasets import fetch_lfw_people
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# downloading the data(labeled faced in the wild)
# from the servers and if the data is already present in the current working
# directory, then load them as numpy array
lfw_people = fetch_lfw_people(data_home="/home/anand/Facial-Recognition/faces", min_faces_per_person=70)

nsamples, h, w = lfw_people.images.shape
# load the data into a variable and its target values and its target values or
# expected values in another variable
X = lfw_people.data
y = lfw_people.target

n_images = X.shape[0]
n_features = X.shape[1]
person_name = lfw_people.target_names
n_classes = person_name.shape[0]


print person_name

#printing the information about the dataset
print "Total dataset size: "
print "# images: %d" % n_images
print "# features: %d" % n_features
print "# classes: %d" % n_classes

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train logisitic regresion
print "Fitting the classifier to the training set"
t0 = time()
logisticreg = LogisticRegression()
logisticreg = logisticreg.fit(X_train, y_train)

print "done in %0.3fs"%(time() - t0)

print "predicting people's naem"
t0 = time()
y_pred = logisticreg.predict(X_test)
print "done in %0.3fs"%(time() -t0)


# Calculate accuracy of current system
num_examples = y_pred.shape[0]
count = 0
for idx in xrange(num_examples):
    if y_pred[idx] == y_test[idx]:
        count += 1

print "Accuracy: %0.3fs" %(count*100.0/num_examples)

with open("model.pkl", "w") as fd:
    pickle.dump(logisticreg,fd)
