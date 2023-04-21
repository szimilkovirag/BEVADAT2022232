import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error


def load_iris_data():
    return load_iris()

def check_data(iris):
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    return iris_df.head(5)

def linear_train_data(iris):
    X = iris.drop('sepal length (cm)', axis=1).values
    y = iris['sepal length (cm)'].values
    return X, y

def logistic_train_data(iris):
    X = iris[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].values
    y = iris.values
    return X, y

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_linear_regression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_logistic_regression(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def predict(model, X_test):
    y_pred = model.predict(X_test)
    return y_pred

def plot_actual_vs_predicted(y_test, y_pred):
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_title('Actual vs Predicted Target Values')
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    plt.show()
    return fig

def evaluate_model(y_test, y_pred):
    mse = np.mean((y_pred - y_test)**2)
    return mse
