"""Question 3 of homework."""
import random
import math


def regression_loss(num_samples, loss_name):
    """
    Calculate regression loss (MAE, MSE, RMSE) for randomly generated samples.

    Parameters:
    num_samples (int): number of samples to generate
    loss_name (str): loss function to use (MAE, MSE, RMSE)
    """
    # Convert num_samples into a string to use .isnumeric
    num_samples_str = str(num_samples)

    # Using .isnumeric() method to check num_samples
    if not num_samples_str.isnumeric():
        return "number of samples must be an integer number"

    # Convert number of samples to an integer
    num_samples = int(num_samples)

    # Make sure that the number of samples must be > 0
    if num_samples <= 0:
        return "number of samples must be greater than 0"

    # Generate random samples using random.uniform
    actual_values = [random.uniform(0, 10) for _ in range(num_samples)]
    predicted_values = [random.uniform(0, 10) for _ in range(num_samples)]

    # Calculate errors
    for i in range(num_samples):
        errors = [abs(actual_values[i] - predicted_values[i])]

    # Assigning different loss_name
    if loss_name == 'MAE':
        loss = sum(errors) / num_samples
    elif loss_name == 'MSE':
        squared_errors = [error ** 2 for error in errors]
        loss = sum(squared_errors) / num_samples
    elif loss_name == 'RMSE':
        squared_errors = [error ** 2 for error in errors]
        mse = sum(squared_errors) / num_samples
        loss = math.sqrt(mse)
    else:
        return "invalid loss function"

    return loss


# Example usage
print(regression_loss(5, 'RMSE'))
