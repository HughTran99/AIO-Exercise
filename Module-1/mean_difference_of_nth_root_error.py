"""Question 5 of homework."""


def md_nre_single_sample(y, y_hat, n, p):
    """
    Calculate the Mean Difference of nth Root Error for a single sample.

    Parameters:
    y: Actual value
    y_hat: Predicted value
    n: Number of observations
    p: Power of the loss function
    """
    # Calculate nth root of y
    y_root = y ** (1 / n)

    # Calculate nth root of y_hat
    y_hat_root = y_hat ** (1 / n)

    # Calculate difference between y and y_hat after rooting
    difference = y_root - y_hat_root

    # Calculate the loss value
    loss = difference ** p

    # Return the loss value
    return loss


# Assertion of the function
result = round(md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1), 2)
assert result == 0.03

# Print the function with some test values
print(md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1))
print(md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1))
print(md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1))
