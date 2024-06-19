"""Question 3."""
import gdown


def words_count(file_path):
    """
    Count the number of words inside a given file path.

    Args:
        file_path: The given file path

    Returns:
        dict: A dictionary containing the word counts.
    """
    # Read the file and put all words in the file into text
    with open(file_path, "r") as file:
        text = file.read()

    # Process the words into lower case
    words = text.split()
    words_lower = [i.lower() for i in words]

    # Get the unique value to turn into the dictionary keys
    words_lower_unique = sorted(list(set(words_lower)))

    # Create an empty dictionary to store the result
    word_count = {}

    # Iterate to count the number of words
    for words in words_lower_unique:
        word_count[words] = words_lower.count(words)

    return word_count


# Download the file using gdown
file_url = "https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko"
output = "P1_data.txt"
gdown.download(file_url, output, quiet=False)

# Test cases:
if __name__ == "__main__":
    file_path = "/content/P1_data.txt"
    print(words_count(file_path))
