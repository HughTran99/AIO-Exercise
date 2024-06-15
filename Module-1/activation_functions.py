"""Question 2 of homework."""
import math


def is_number(x):
    """Check if x is a number."""
    try:
        float(x)
    except ValueError:
        return False
    return True


def calc_activation_function(x, activation_function):
    """Calculate the specified activation function."""
    # Check if x is a number
    if not is_number(x):
        return 'x must be a number'

    # Convert x to float
    x = float(x)

    # Define alpha for ELU
    alpha = 0.01

    if activation_function == 'sigmoid':
        # Formula of Sigmoid function
        return 1 / (1 + math.exp(-x))
    elif activation_function == 'relu':
        # Formula of ReLU function
        return x if x > 0 else 0
    elif activation_function == 'elu':
        # Formula of ELU function
        return x if x > 0 else alpha * (math.exp(x) - 1)
    else:
        # Response when an unsupported activation function is entered
        return f'{activation_function} is not supported'


# Example of the function
print(calc_activation_function(2, 'belu'))
print(calc_activation_function('asd', 'relu'))
print(calc_activation_function(-1, 'elu'))
