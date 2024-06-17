import re


def characters_counting(string):
    """
    Count the number of characters in a string.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary containing the character counts.
    """
    # Ensure the input string must be [a-z] or [A-Z]
    if not re.match("^[a-zA-Z]*$", string):
        print("Input must contain only letters from a-z or A-Z")
        return False

    # Create an empty dictionary to store the result
    char_count = {}

    # Get the unique characters, turn it into a sorted list
    unique_char = sorted(list(set(string)))

    # Iterate to count the number of characters
    for character in unique_char:
        char_count[character] = string.count(character)

    return char_count


# Test cases:
if __name__ == "__main__":
    string = "Happiness"
    assert characters_counting(string) == {
        "H": 1, "a": 1, "e": 1, "i": 1, "n": 1, "p": 2, "s": 2}

    input_string = input("Input string: ")
    result = characters_counting(input_string)
    print(result)
