def getCardPoints(winning_numbers: list, owned_numbers: list) -> int:
    """Find the matching winning cards against the owned cards
    
    Inputs:
        winning_numbers: list of winning numbers
        owned_numbers: list of owned numbers

    Returns:
        int: length of the list of matching numbers
    """

    earned_points = [i for i in owned_numbers if i in winning_numbers]

    return len(earned_points)

def scratchcards(cards: list) -> int:
    """Main function that returns the total number of scratch cards points."""
    total = 0

    for i in range(len(cards)):
        winning_numbers = cards[i].split('|')[0].split(':')[1].split()
        owned_numbers = cards[i].split('|')[1].split()

        current_card_points = getCardPoints(winning_numbers, owned_numbers)
        total += 2**(current_card_points -1) if current_card_points > 0 else 0

    return total


if __name__ == '__main__':
    with open('../input.txt') as f:
        cards = [line.rstrip() for line in f]

    print(scratchcards(cards))
