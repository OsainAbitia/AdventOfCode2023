from cube_conundrum import cubeConundrum

def test_basic_example_is_ok():
    test_array = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
    assert cubeConundrum(test_array) == 2286

def test_basic_example_two():
    test_array = [
        "Game 1: 1 blue, 1 red; 4 red, 2 green, 6 blue; 8 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 6 green, 20 blue",
        "Game 3: 8 green, 6 blue, 2 red; 5 blue, 4 red, 13 green; 25 green, 19 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 20 blue, 18 red, 20 green"
        ]
    assert cubeConundrum(test_array) == 10992

def test_all_same_value():
    test_array = [
        "Game 1: 1 blue, 1 red; 1 red, 1 green, 1 blue; 1 green",
        "Game 2: 1 blue, 1 green; 1 green, 1 blue, 1 red; 1 green, 1 blue",
        "Game 3: 1 green, 1 blue, 1 red; 1 blue, 1 red, 1 green; 1 green, 1 red",
        "Game 4: 1 green, 1 red, 1 blue; 1 green, 1 red; 1 green, 1 blue, 1 red",
        "Game 5: 1 red, 1 blue, 1 green; 1 blue, 1 red, 1 green"
        ]
    assert cubeConundrum(test_array) == 5
