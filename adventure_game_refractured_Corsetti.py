# Udacity Adventure Game Project
# Margo Corsetti
# 23 May 2021

import time
import random
items = []
creature_list = ["wicked fairie", "troll", "dragon"]


def print_pause(string):
    print(string)
    time.sleep(2)


def intro(items):
    items.clear()
    creature = random.choice(creature_list)
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + creature +
                " is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")
    return creature


def field(items, creature):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choose_location(items, creature)


def choose_location(items, creature):
    user_choice = input("What would you like to do\n"
                            "(Please enter 1 or 2).\n")
    if user_choice == '1':
        house(items, creature)
    elif user_choice == '2':
        cave(items, creature)
    else:
        print_pause("Sorry, I don't understand")
        choose_location(items, creature)


def choose_action():
    fight_or_run = input("Would you like to do"
                             " (1) fight or (2) run away\n")
    if fight_or_run != '1' and fight_or_run != '2':
        print_pause("Sorry, I don't understand")
        choose_action()
    return fight_or_run


def restart():
    play_again = input("Would you like to play again? (y/n)")
    if play_again.lower() == 'n':
        print("Thanks for playing. See you next time.")
    elif play_again.lower() == 'y':
        print_pause("Excellent! Restarting the game")
        play_game()
    else:
        print_pause("Sorry, I don't understand.")
        restart()


def house(items, creature):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                " and out steps a " + creature + ".")
    print_pause("Eep! This is the " + creature + "\'s house!")
    print_pause("The " + creature + " attacks you!")
    if 'sword' in items:
        action = choose_action()
        if action == '1':
            print_pause("As the " + creature + " moves to attack,"
                        " you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand"
                        " as you brace yourelf for the attack.")
            print_pause("But the " + creature + " takes one look"
                        " at your shiny new toy and runs away!")
            print_pause("You have rid the town of the " + creature + "."
                        " You are victorious!")
            restart()
        elif action == '2':
            print_pause("You run back into the field."
                        " Luckily, you don't seem to have been followed.")
            field(items, creature)
    else:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
        action = choose_action()
        if action == '1':
            print_pause("You do your best...")
            print_pause("but your dagger is no match"
                        " for the " + creature + ".")
            print_pause("You have been defeated!")
            restart()
        elif action == '2':
            print_pause("You run back out to the field.")
            field(items, creature)


def cave(items, creature):
    print_pause("you peer cautiously into the cave.")
    if 'sword' in items:
        print_pause("You've been here before, and gotten al the good stuff."
                    " It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        items.append('sword')
    print_pause("You walk back out to the field.\n")
    field(items, creature)


def play_game():
    creature = intro(items)
    field(items, creature)


play_game()
