import numpy as np

class Perceptron:
    def __init__(self, input_size, lr=0.1, epochs=10):
        self.weights = np.zeros(input_size)
        self.bias = 0.0
        self.lr = lr
        self.epochs = epochs

    def predict(self, x):
        z = np.dot(x, self.weights) + self.bias
        return 1 if z >= 0 else 0

    def train(self, X, Y):
        for _ in range(self.epochs):
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = Y[i] - prediction
                self.weights += self.lr * error * X[i]
                self.bias += self.lr * error

X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([0, 0, 0, 1])

model = Perceptron(input_size=2)
model.train(X, Y)

print("NumPy Perceptron AND Gate Results:")
for x in X:
    print(f"Input: {x} -> Predicted: {model.predict(x)}")

print(f"\nFinal Weights: {model.weights}")
print(f"Final Bias: {model.bias}")
