def scratchcards(cards: str) -> int:
    total = 0
    for card in cards:
        earned_points = 0

        wining_numbers = card.split('|')[0].split(':')[1].split()
        scratch_numbers = card.split('|')[1].split()
        
        matches = [i for i in scratch_numbers if i in wining_numbers]

        if len(matches) >= 1:
            earned_points += 1
            for match in matches[1:]:
                earned_points = earned_points * 2

        total += earned_points
    
    return total

if __name__ == '__main__':
    with open('../input.txt') as f:
        cards = [line.rstrip() for line in f]

    print(scratchcards(cards))