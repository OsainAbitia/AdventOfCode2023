from gear_ratios import gearRatios

def testBasicExample():
    board = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]
    assert gearRatios(board) == 4361