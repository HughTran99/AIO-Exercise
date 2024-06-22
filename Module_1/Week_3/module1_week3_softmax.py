"""Question 1 of homework."""


import torch
import torch.nn as nn


class Softmax(nn.Module):
    """Compute the softmax value for each input in the given tensor."""

    def __init__(self):
        """Initialize the attributes from PyTorch."""
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


class SoftmaxStable(nn.Module):
    """Compute the stable softmax value for each input in the given tensor."""

    def __init__(self):
        """Initialize the attributes from PyTorch."""
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


# Test cases
if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    softmax_stable = SoftmaxStable()
    print(softmax(data))
    print(softmax_stable(data))
