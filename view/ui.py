def display_cards(who):
    """Turn the player's cards into a single string of cards, which is returned."""
    cards = ""
    for card in who:
        cards = cards + "   " + card[0] 
    return cards

