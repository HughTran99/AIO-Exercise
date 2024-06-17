"""Question 1."""


def max_kernel(num_list, k):
    """
    Scan the max volume of the sliding window and create a new list.

    Input:
        num_list: The input list
        k (int): The size of the sliding window

    Output:
        max_values: The list of max values
    """
    # Check condition for k
    try:
        k = int(k)
    except ValueError:
        print("k must be an integer")
        return False
    if k <= 0:
        print("k must be greater than 0")
        return False

    # Initialize variables
    result = []
    max_values = []

    # Iterate num_list to scan for max value
    for i in num_list:
        result.append(i)
        if len(result) == k:
            max_values.append(max(result))
            result.pop(0)

    return max_values


# Test cases
if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44]
    assert max_kernel(num_list, k=3) == [5, 5, 5]

    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = input("Input k: ")
    print(max_kernel(num_list, k))
