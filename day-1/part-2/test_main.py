# Tests from SlowFlo, they helped me to understand and find the reason
# my code was not working at all and comprehend the use of tests!
# visit his repo on https://github.com/SlowFlo/advent_of_code_2023/blob/main/.gitignore
from main import getCalibrationValuesWithStrings

def test_one_digit_is_found_twice():
    assert getCalibrationValuesWithStrings(["1"]) == 11
    assert getCalibrationValuesWithStrings(["2"]) == 22


def test_2_digits_is_the_same():
    assert getCalibrationValuesWithStrings(["23"]) == 23


def test_3_digits_is_without_the_middle_one():
    assert getCalibrationValuesWithStrings(["456"]) == 46
    assert getCalibrationValuesWithStrings(["789"]) == 79


def test_has_letters_between_is_ok():
    assert getCalibrationValuesWithStrings(["1abc2"]) == 12


def test_has_letters_on_sides_is_ok():
    assert getCalibrationValuesWithStrings(["pqr3stu8vwx"]) == 38


def test_advanced_examples_are_ok():
    assert getCalibrationValuesWithStrings(["a1b2c3d4e5f"]) == 15
    assert getCalibrationValuesWithStrings(["treb7uchet"]) == 77

def test_sum_of_multi_line_file_is_ok():
    array = [
                "1abc2",
                "pqr3stu8vwx",
                "a1b2c3d4e5f",
                "treb7uchet",
            ]

    assert getCalibrationValuesWithStrings(array) == 142


def test_detect_digits_written_with_letters():
    assert getCalibrationValuesWithStrings(["two1nine"]) == 29


def test_two_merged_spelled_out_digits_with_digits_in_middle_is_ok():
    assert getCalibrationValuesWithStrings(["eightwothree"]) == 83


def test_two_merged_spelled_out_digits_with_common_letter_are_two_digits():
    assert getCalibrationValuesWithStrings(["eighthree"]) == 83
    assert getCalibrationValuesWithStrings(["sevenine"]) == 79


def test_more_advanced_examples_are_ok():
    assert getCalibrationValuesWithStrings(["abcone2threexyz"]) == 13
    assert getCalibrationValuesWithStrings(["xtwone3four"]) == 24
    assert getCalibrationValuesWithStrings(["4nineeightseven2"]) == 42
    assert getCalibrationValuesWithStrings(["zoneight234"]) == 14
    assert getCalibrationValuesWithStrings(["7pqrstsixteen"]) == 76


def test_sum_of_advanced_multi_line_file_is_ok():
    array = [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen"
            ]

    assert getCalibrationValuesWithStrings(array) == 281