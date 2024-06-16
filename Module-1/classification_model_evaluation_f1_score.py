"""Question 1 of homework."""
import math


def f1_score_evaluation(tp, fp, fn):
    """
    Calculate the F1 score.

    Parameters:
    tp (int): True positive
    fp (int): False positive
    fn (int): False negative
    """
    # Check the function to make sure that tp, fp, and fn are integers
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        return 'tp, fp, and fn must be int'

    # Check the function to make sure that tp, fp, and fn are greater than 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        return 'tp, fp, and fn must be greater than zero'

    # Calculate the Precision value
    precision = tp / (tp + fp)

    # Calculate the Recall value
    recall = tp / (tp + fn)

    # Calculate the F1 score
    f1_score = 2 * precision * recall / (precision + recall)

    # Return the desired F1 score
    return f1_score


# Assertion check
assert round(f1_score_evaluation(tp=2, fp=3, fn=4), 2) == 0.36

# Test F1 score result
print(f1_score_evaluation(tp=4, fp=9, fn=6))
