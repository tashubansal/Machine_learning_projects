from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np


def flower_prediction(*input_features):
    from sklearn import datasets
    iris=datasets.load_iris()
    features=iris.data
    labels=iris.target
    # X_train,X_test,Y_train,Y_test=train_test_split(features,labels,test_size=0.20,random_state=0)

    model=KNeighborsClassifier()
    # model.fit(X_train,Y_train)
    model.fit(features,labels)
# plt.scatter(X_train[:,0],Y_train[:])
# plt.xlabel("Sepal Length")
# plt.ylabel("Flower Type")
# plt.show()
    a=np.array(input_features,dtype=float)
    a=a.reshape(1,-1)
    return model.predict(a)

    # a=accuracy_score(predictions,)
    # print("Accuracy:",a)
# flower_prediction(input_features)    