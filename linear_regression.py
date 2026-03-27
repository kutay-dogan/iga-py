import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

class LinearRegression:
    def __init__(self, lr=0.01, iterations=1000):
        self.lr = lr
        self.iterations = iterations
        self.weights = None
        self.bias = None
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        for i in range(self.iterations):
            # y = wx+b
            y_pred = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = np.mean(y_pred-y)

            self.weights -= self.lr*dw
            self.bias -= self.lr*db

            if i%100 == 0:
                mse = np.mean((y-y_pred)**2)
                print(f"Iteration: {i}, Loss: {(mse):.3f}")

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
    

def main():
    diabetes = datasets.load_diabetes(scaled=True)
    X = diabetes.data
    y = diabetes.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression(lr=0.05,iterations=10000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = np.mean(np.abs(y_test-predictions))

    print(f"MAE: {(mae):.3f}")

main()