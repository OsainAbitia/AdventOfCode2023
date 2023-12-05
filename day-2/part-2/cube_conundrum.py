def cubeConundrum(lines):
    total = 0
    
    # Evaluate each game
    for line in lines:
        game_set = line.split(':') # Segregate game id from rounds
        rounds = game_set[1].replace(';', ',').split(',') # Segregate rounds from each other
        current_max = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        # Evaluate each cube returned in a round
        for cube in rounds:
            cube = cube.strip().split(' ')
            count, color = int(cube[0]), cube[1]
           
            # Update max count for current color
            current_max[color] = max(current_max[color], count)

        total += current_max['red'] * current_max['green'] * current_max['blue']
    
    return total
            
if __name__ == '__main__':
    with open('../input.txt') as f:
        lines = [line.rstrip() for line in f]
    print(cubeConundrum(lines))