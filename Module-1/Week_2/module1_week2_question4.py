"""Question 4."""
import re


def levenshtein_distance(w1, w2):
    """
    Compute the Levenshtein distance between two words.

    Args:
        w1 (str): The first word.
        w2 (str): The second word.

    Returns:
        int: The Levenshtein distance between w1 and w2.
    """
    # Ensure the input string must be [a-z] or [A-Z]
    if not re.match("^[a-zA-Z]*$", w1) or not re.match("^[a-zA-Z]*$", w2):
        print("Input must contain only letters from a-z or A-Z")
        return False

    # Calculate the dimensions of the matrix
    d_length = len(w1) + 1
    d_height = len(w2) + 1

    # Create an empty matrix to store the result
    d = [[0] * d_length for _ in range(d_height)]

    # Fill index value into the matrix
    for i in range(d_length):
        d[0][i] = i
    for j in range(d_height):
        d[j][0] = j

    # Iterate to calculate the Levenshtein distance
    for m in range(1, d_height):
        for n in range(1, d_length):
            if w2[m-1] == w1[n-1]:
                d[m][n] = d[m-1][n-1]
            else:
                d[m][n] = min(d[m - 1][n], d[m][n - 1], d[m - 1][n - 1]) + 1

    return d[d_height - 1][d_length - 1]


# Test cases:
if __name__ == "__main__":
    w1 = "you"
    w2 = "yu"
    assert levenshtein_distance(w1, w2) == 1

    w1 = input("input word 1: ")
    w2 = input("input word 2: ")
    print(levenshtein_distance(w1, w2))
