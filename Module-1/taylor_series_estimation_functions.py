"""Question 4 of homework."""
import math


def taylor_series_sin(x, n):
    """
    Taylor series approximation of sin(x).

    Parameters:
    x (float): input angle in radians
    n (int): number of loops to include in the series
    """
    # Condition of n
    if n <= 0:
        return 'The number of n must be greater than 0'

    # Initiation of sin(x)
    sin_x = 0
    for i in range(n+1):
        loops = (-1)**i * x**(2*i+1) / math.factorial(2*i+1)
        sin_x += loops

    return sin_x


print(taylor_series_sin(x=3.14, n=10))


def taylor_series_cos(x, n):
    """
    Taylor series approximation of cos(x).

    Parameters:
    x (float): input angle in radians
    n (int): number of loops to include in the series
    """
    # Condition of n
    if n <= 0:
        return 'The number of n must be greater than 0'

    # Initiation of cos(x)
    cos_x = 0
    for i in range(n+1):
        loops = (-1)**i * x**(2*i) / math.factorial(2*i)
        cos_x += loops

    return cos_x


print(taylor_series_cos(x=3.14, n=10))


def taylor_series_sinh(x, n):
    """
    Taylor series approximation of sinh(x).

    Parameters:
    x (float): input angle in radians
    n (int): number of loops to include in the series
    """
    # Condition of n
    if n <= 0:
        return 'The number of n must be greater than 0'

    # Initiation of sinh(x)
    sinh_x = 0
    for i in range(n+1):
        loops = x**(2*i+1) / math.factorial(2*i+1)
        sinh_x += loops

    return sinh_x


print(taylor_series_sinh(x=3.14, n=10))


def taylor_series_cosh(x, n):
    """
    Taylor series approximation of cosh(x).

    Parameters:
    x (float): input angle in radians
    n (int): number of loops to include in the series
    """
    # Condition of n
    if n <= 0:
        return 'The number of n must be greater than 0'

    # Initiation of cosh(x)
    cosh_x = 0
    for i in range(n+1):
        loops = x**(2*i) / math.factorial(2*i)
        cosh_x += loops

    return cosh_x


print(taylor_series_cosh(x=3.14, n=10))
