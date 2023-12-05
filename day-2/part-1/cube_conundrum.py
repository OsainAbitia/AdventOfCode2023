def cubeConundrum(lines):
    total = 0
    existing_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    
    # Evaluate each game
    for line in lines:
        game_set = line.split(':') # Segregate game id from rounds
        game_id = int("".join(filter(str.isdigit, game_set[0])))
        rounds = game_set[1].replace(';', ',').split(',') # Segregate rounds from each other
        is_valid = True # Flag to identify if we got more cubes that are allowed

        # Evaluate each cube returned in a round
        for cube in rounds:
            cube = cube.strip().split(' ')
            count, color = int(cube[0]), cube[1]
           
            current_limit = existing_cubes[color]
            if count > current_limit:
                is_valid = False
                break

        if is_valid:
            total += game_id
    
    return total
            
if __name__ == '__main__':
    with open('../input.txt') as f:
        lines = [line.rstrip() for line in f]
    print(cubeConundrum(lines))