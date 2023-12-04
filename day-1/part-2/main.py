import re

def cleanCalibrationCode(line: str) -> str:
    """Returns the calibration code numbers only."""
    def replace_with_digit(match_object: re.Match):
        # keeping one letter on each side for twone => 21 cases
        nums_and_letters = {
            'one': 'o1e',
            'two': 't2o',
            'three': 't3e',
            'four': 'f4r',
            'five' : 'f5e',
            'six': 's6x',
            'seven': 's7n',
            'eight': 'e8t',
            'nine': 'n9e'
        }

        return nums_and_letters[match_object.group(0)]
    
    line = re.sub(
        r"one|two|three|four|five|six|seven|eight|nine",
        replace_with_digit,
        line,
    )
    
    # doing once more for the few remaining cases
    line = re.sub(
        r"one|two|three|four|five|six|seven|eight|nine",
        replace_with_digit,
        line,
    )
    return line

def getCalibrationValuesWithStrings(lines: list) -> int:
    """Returns the secret code total sum inside the calibration code."""
    total_calibration_sum = 0
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five' : '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    pattern = '|'.join(numbers.keys())

    for code in lines:
        code = cleanCalibrationCode(code)
        numbers_found = re.findall(f'(?:{pattern})|\d', code)
        
        # Identify first digit
        first_digit = numbers_found[0]
        second_digit = numbers_found[len(numbers_found) - 1]
        
        # Turn the numbers to ints and sum
        if first_digit in numbers:
            first_digit = numbers[first_digit]
        if second_digit in numbers:
            second_digit = numbers[second_digit]

        current_sum = first_digit + second_digit
        total_calibration_sum += int(current_sum)

    print(f" Total sum exercise 2: {total_calibration_sum}")
    return total_calibration_sum

if __name__ == '__main__':

    with open('../input.txt') as f:
        lines = [line.rstrip() for line in f]
        getCalibrationValuesWithStrings(lines)