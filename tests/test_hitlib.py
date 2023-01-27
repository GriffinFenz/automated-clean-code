from automated_clean_code.exercise_20_histlib import find_max_and_min_key, get_lines_from_file


def test_get_lines_from_file():
    output = {"Superman 1": 1, "Superman 2": 1, "Superman 3": 2, "": 1}
    output2 = {"a": 7, "": 3, "ap": 10}
    assert output == get_lines_from_file(
        "/Users/naphong/Desktop/Uni/softwareeng/automated-clean-code/tests/superman.txt"
    )
    assert output2 == get_lines_from_file("/Users/naphong/Desktop/Uni/softwareeng/automated-clean-code/tests/ap.txt")


def test_find_max_and_min_key():
    output = ("", 3, "ap", 10)
    assert output == find_max_and_min_key(
        get_lines_from_file("/Users/naphong/Desktop/Uni/softwareeng/automated-clean" "-code/tests/ap.txt")
    )
