# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
from typing import Dict


def find_max_min_from_file(filename: str):
    """
    Find most common and least common key in a file.

    It takes one argument, filename, which is the name of a file to read from.
    The function returns two values: min_line and max_line.

    :param filename:str: Pass in the name of the file to be read
    :return: The min key and the max key
    :doc-author: Trelent
    """
    line_counts: Dict[str, int] = get_lines_from_file(filename)  # pragma: no cover
    min_line, amount_for_min, max_line, amount_for_max = find_max_and_min_key(line_counts)  # pragma: no cover
    print(f"Min Key = {min_line} with count = {amount_for_min}")  # pragma: no cover
    print(f"Max Key = {max_line} with count = {amount_for_max}")  # pragma: no cover


def get_lines_from_file(filename: str) -> Dict[str, int]:
    """
    Turn all the line from a file into a dictionary with counts for each line.

    :param filename:str: Specify the file that we want to open
    :return: A dictionary of the lines in a file and how many times they appear
    :doc-author: Trelent
    """
    line_counts: Dict[str, int] = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line in line_counts:
                line_counts[line] += 1
            else:
                line_counts[line] = 1
    return line_counts


def find_max_and_min_key(line_counter: Dict[str, int]) -> (str, int, str, int):
    """
    Find the most common and least common keys in a dictionary.

    :param line_counter:Dict[str: Store the line and count of each line
    :param int]: Cast the return value of line_counter
    :return: The key with the highest count and the lowest count
    :doc-author: Trelent
    """
    max_key = None
    max_counter: int = 0
    min_key = None
    min_counter: int = 0
    for line, count in line_counter.items():
        if max_key is None or count > max_counter:
            max_key = line
            max_counter = count
        if min_key is None or count < min_counter:
            min_key = line
            min_counter = count
    return min_key, min_counter, max_key, max_counter


def main():
    """
    Run the function to get most and least common line in a file.

    :return: The max and min value from the file
    :doc-author: Trelent
    """
    find_max_min_from_file(
        "/Users/naphong/Desktop/Uni/softwareeng/automated-clean-code/tests/ap.txt"
    )  # pragma: no cover


if __name__ == "__main__":
    main()
