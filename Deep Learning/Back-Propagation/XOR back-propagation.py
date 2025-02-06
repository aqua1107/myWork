import numpy as np
import matplotlib.pyplot as plt

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR input and output data (using the data from the original example)
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])  # Adjusted input data (4 samples, 3 features, third index is a bias)
y = np.array([[0], [1], [1], [0]])  # Output remains the same

# Neural network settings
input_layer_neurons = 3  # Number of input nodes (number of columns in X)
hidden_layer_neurons = 2  # Number of hidden nodes
output_layer_neurons = 1  # Number of output nodes

# Given weights and biases
w_input_hidden = np.array([[0.4, -0.3], [-0.35, 0.45], [0.3, 0.3]])  # Input to hidden layer weights (3, 2)
w_hidden_output = np.array([[0.5], [-0.6]])  # Hidden to output layer weights (2, 1)

# Random initialization for biases
hidden_bias = np.random.rand(1, hidden_layer_neurons)  # Bias for hidden layer (1, 2)
output_bias = np.random.rand(1, output_layer_neurons)  # Bias for output layer (1, 1)

# Learning rate and number of epochs
learning_rate = 0.02
epochs = 100000

# List to store error values for plotting
error_list = []

# Training the neural network
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X, w_input_hidden) + hidden_bias  # Shape (4, 2)
    hidden_layer_output = sigmoid(hidden_layer_input)  # Shape (4, 2)

    output_layer_input = np.dot(hidden_layer_output, w_hidden_output) + output_bias  # Shape (4, 1)
    predicted_output = sigmoid(output_layer_input)  # Shape (4, 1)

    # Error calculation
    error = y - predicted_output
    error_list.append(np.mean(np.abs(error)))  # Store the error for plotting
    
    if epoch % 1000 == 0:
        print(f'Epoch {epoch} Error: {np.mean(np.abs(error))}')
    
    # Backpropagation
    # Output layer error gradient
    output_error = error * sigmoid_derivative(predicted_output)
    
    # Hidden layer error gradient
    hidden_error = output_error.dot(w_hidden_output.T) * sigmoid_derivative(hidden_layer_output)
    
    # Update weights and biases
    w_hidden_output += hidden_layer_output.T.dot(output_error) * learning_rate
    output_bias += np.sum(output_error, axis=0, keepdims=True) * learning_rate
    w_input_hidden += X.T.dot(hidden_error) * learning_rate
    hidden_bias += np.sum(hidden_error, axis=0, keepdims=True) * learning_rate

# Final output
print("\nFinal Output after Training:")
print(predicted_output)

# Plot error graph
plt.plot(np.arange(epochs), error_list)
plt.title("Error graph")
plt.xlabel("Epochs")
plt.ylabel("Error")
plt.show()
