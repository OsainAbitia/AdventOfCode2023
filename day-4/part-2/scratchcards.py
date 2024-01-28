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
    """Main function that returns the total number of scratch cards."""

    scratchcards_copies = {}

    for i in range(len(cards)):
        winning_numbers = cards[i].split('|')[0].split(':')[1].split()
        owned_numbers = cards[i].split('|')[1].split()

        current_card_points = getCardPoints(winning_numbers, owned_numbers)

        for j in range(current_card_points):
            current_key = i + j + 1
            current_copies = scratchcards_copies.get(i, 0)

            # If we have no copies of the current card, we just got 1 copy of the
            # next n cards where n is the number of current card points
            if current_copies == 0:
                scratchcards_copies[current_key] = 1
            # If the current card does have copies, then instead of adding 1 copy
            # we add the number of copies + 1 to the next n cards
            else:
                scratchcards_copies[current_key] = scratchcards_copies.get(current_key, 0) + current_copies + 1

    return sum(scratchcards_copies.values()) + len(cards)

if __name__ == '__main__':
    with open('../input.txt') as f:
        cards = [line.rstrip() for line in f]

    print(scratchcards(cards))
