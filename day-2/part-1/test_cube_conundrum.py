from cube_conundrum import cubeConundrum

def test_basic_example_is_ok():
    test_array = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
    assert cubeConundrum(test_array) == 8

def test_all_valid_games():
    test_array = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
    assert cubeConundrum(test_array) == 15

def test_all_invalid_games():
    test_array = [
        "Game 1: 15 blue",
        "Game 3: 14 green",
        "Game 5: 13 red"
        ]
    assert cubeConundrum(test_array) == 0

def test_all_valid_games_with_maximum_allowed():
    test_array = [
        "Game 1: 14 blue",
        "Game 3: 13 green",
        "Game 5: 12 red"
        ]
    assert cubeConundrum(test_array) == 9