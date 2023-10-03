import random
import time

## import data  # Makes sure you put data. in front of all function calls.

from model.data import make_deck, init_deck_values
from calcs import calc_total, determine_ace_value
from view.ui import display_cards
from rich.console import Console

console = Console()
deck_values = init_deck_values()


def draw():
    """Select a random card from the deck. The deck shrinks by 1."""
    selection = random.choice(deck)
    deck.remove(selection)
    return selection, deck_values[selection]


def display_status():
    return f"""
    Here are your cards: {display_cards(player)}

    Here is your current score: {calc_total(player)}

    Here is the dealer's card: {dealer[0][0]}
    """  

def add_card(who):
    """Given a player or dealer list, add another card to the list."""
    selection = draw()
    if isinstance(selection[-1], list):
        who.append((selection[0], determine_ace_value(who)))  # We have an Ace.
    else:
        who.append(selection)    


deck = make_deck()


player = []
dealer = []

player.append(draw())
dealer.append(draw())
player.append(draw())
dealer.append(draw())

still_running = True

def restartGame():
    player.clear()
    dealer.clear()
    player.append(draw())
    dealer.append(draw())
    player.append(draw())
    dealer.append(draw())

if __name__ == "__main__":   # Is Python running directly (or imported)?
    
    console.print("Welcome to [red]BLACKJACK[/] , the home of [green]FREEEE[/] money!!!\n", style="bold underline purple")
    
    while still_running == True:
        while True:
            console.print("Here is your first hand:", style="bold blue")
            print(display_status())
            console.print("[bold]Will you [green]hit[/] (for winning) or [red]stand[/] (you want to lose)? Press [green]'h'[/] or [red]'s'[/] to decide[/]")
            choice = input()

            if choice in ['h', 'H']:
                add_card(player)
                if calc_total(player) >= 21 :
                    break
            elif choice in ['s', 'S']:
                break
            else:
                console.print("Oh come on, seriously? Can't even follow simple instructions, I said choose [green]'h'[/] or [red]'s'[/].", style="bold blue")

        keep_playing = True
        if calc_total(player) > 21:
            print(display_status())
            console.print("Damn you went BUST! Well you know what they say [purple]97%[/] of miners quit just before they strike diamond, so [blue]try again![/] ", style="bold underline red")
            keep_playing = False
        elif calc_total(player) == 21:
            print(display_status())
            console.print("[purple]HOLY MOLY![/] You hit a 21! WOWWZA that's amazing! [green]YOuuuuu WINNN!!![/]", style="bold underline blue")
        else:
            print("Current state of game:")
            print(display_status())

        if keep_playing:
            while True:
                console.print("Here are the dealer's cards:", style="bold red")
                print(display_cards(dealer))
                if calc_total(dealer) < 17 :
                    add_card(dealer)
                    console.print("Dealer has chosen to hit, here are his cards:", style="bold underline red")
                    print(display_cards(dealer))
                if calc_total(dealer) >= 22:
                    console.print("[red]The dealer has LOST![/] What a loser amirite! Hahahah, you're like way cooler because [green]YOU WON![/]", style="bold underline blue")
                    break
                elif calc_total(dealer) >= 17:
                    break
                elif calc_total(dealer) < calc_total(player):
                        console.print("[purple]HOLY MOLY![/] You WONNN! WOWWZA that's amazing! [green]YOuuuuu WINNN :confetti_ball: !!![/]", style="bold underline blue")
                        break
                time.sleep(1)
        else:
            console.print("Only [red]loosers[intentionally mispelled](YOU)[/] could lose to a computer :skull:", style="bold underline purple")
            if calc_total(dealer) > calc_total(player):
                console.print("Only [red]loosers[intentionally mispelled](YOU)[/] could lose to a computer :skull:", style="bold underline purple")
        
        console.print("[bold]Surely you'll play again right? Theres so much money to be made! Press [green]'y'[/] for yes and [red]'n'[/] for no (the wrong option)[/]")
        reset = input()
        if reset in ['y', 'Y']:
            restartGame()
        if reset in ['n', 'N']:
            exit()