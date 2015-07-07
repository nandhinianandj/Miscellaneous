# Self test or testing on same data as trained-- susceptible to overfitting

from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
Y = iris.target

print "Testing and trainnig on same data set"
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()

logreg.fit(X, Y)

logreg_y_pred = logreg.predict(X)

# Find metrics
from sklearn import metrics
print "Logistic Regression", metrics.accuracy_score(Y, logreg_y_pred)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, Y)
knn_5_y_pred = knn.predict(X)
print "k-nearest neighbor (5)" , metrics.accuracy_score(Y, knn_5_y_pred)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, Y)
knn_1_y_pred = knn.predict(X)
print "k-nearest neighbor (1)" , metrics.accuracy_score(Y, knn_1_y_pred)


print "Test and Train on split datasets"
# Train/test Split --knn {1}

# Train/test Split --knn {5}
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=4)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
logreg_y_pred = logreg.predict(X_test)
print metrics.accuracy_score(y_test, logreg_y_pred)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print metrics.accuracy_score(y_test, y_pred)

# plot k nn accuracy for a range of k-values
k_range = range(1,36)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

print k_range, scores
import matplotlib.pyplot as plt
plt.plot(k_range, scores)
plt.xlabel('Value of K- KNN')
plt.ylabel('Test Accuracy')


