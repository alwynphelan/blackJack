
def calc_total(who):
    """Work out the player's total (dealer/player) taking Aces into account.
    The assumption is that the value of 'who' is a list of cards."""
    other_cards_total = 0
    aces_count = 0

    for card in who:
        if isinstance(card[-1], list):
            aces_count = aces_count + 1
        else:
            other_cards_total = other_cards_total + card[-1]

    if aces_count:
        # We have AT LEAST one Ace.
        if other_cards_total <= 10:
            if aces_count == 1:
                return other_cards_total + 11
            if aces_count == 2:
                if other_cards_total < 10:
                    return other_cards_total + 11 + 1
                else:
                    return other_cards_total + aces_count
            if aces_count == 3:
                if other_cards_total < 9:
                    return other_cards_total + 11 + 1 + 1
                else:
                    return other_cards_total + aces_count
            if aces_count == 4:
                if other_cards_total < 8:
                    return other_cards_total + 11 + 1 + 1 + 1
                else:
                    return other_cards_total + aces_count               
        else:
            return other_cards_total + (aces_count)
    else:
        return other_cards_total


def determine_ace_value(who):
    """Based on the value of calc_total, return either 11 or 1."""
    if calc_total(who) <= 10:
        return 11
    return 1

