import time
import random


def print_wait(message_to_print):
    time.sleep(2)
    print(message_to_print)


weapon_list = ['the magical Sword of Ogoroth', 'magic knife',
               'magic staff']
enemies = ['wicked fairie', 'troll', 'vampire']


def play_game():
    enemy_index = random.randint(0, len(enemies) - 1)
    enemy = enemies[enemy_index]
    weapon = 'dagger'

    def field(enemy, weapon):

        print_wait('You find yourself standing in an open field'
                   + ', filled with grass and yellow wildflowers.'
                   )
        print_wait('Rumor has it that a ' + enemy + ' is'
                   + 'somewhere around here, and has been'
                   + ' terrifying the nearby village.'
                   )
        print_wait('In front of you is a house.')
        print_wait('To your right is a dark cave.')
        print_wait('In your hand you hold your trusty'
                   + ' (but not very effective) dagger.'
                   )
        action(enemy, weapon)

    def action(enemy, weapon):
        print_wait('Enter 1 to knock on the door of the house.')
        print_wait('Enter 2 to peer into the cave.')
        print_wait('What would you like to do?')

        while True:
            choice = input('(Please enter 1 or 2).\n')

            if '1' == choice:
                house(enemy, weapon)
                break
            elif '2' == choice:

                cave(enemy, weapon)
                break

    def fight(enemy, weapon):
        if weapon == 'dagger':
            print_wait('You do your best...')
            print_wait('but your ' + weapon + ' is no match for the '
                       + enemy + '.')
            print_wait('You have been defeated!')
        else:

            print_wait('As the ' + enemy
                       + ' moves to attack, you unsheath your new weapon.'
                       )
            print_wait('The ' + weapon + ' shines brightly in your'
                       + ' hand as you brace yourself for the attack.'
                       )
            print_wait('But the ' + enemy
                       + ' takes one look at your shiny new toy and runs away!'
                       )
            print_wait('You have rid the town of the ' + enemy
                       + '. You are victorious!')

        while True:
            choice = input('Would you like to play again? (y/n)')

            if 'y' == choice:
                print("\n")
                play_game()
                break
            elif 'n' == choice:

                print_wait('Thanks for playing! See you next time.')
                break

    def cave(enemy, weapon):
        print_wait('You peer cautiously into the cave.')

        if weapon == 'dagger':
            print_wait('It turns out to be only a very small cave.')
            print_wait('Your eye catches a glint of metal behind a rock.'
                       )
            weapon_index = random.randint(0, len(weapon_list) - 1)
            weapon = weapon_list[weapon_index]
            print_wait('You have found ' + weapon + '!')
            print_wait('You discard your silly old dagger and'
                       + ' take the sword with you.'
                       )
        else:

            print_wait('You\'ve been here before, and gotten all'
                       + ' the good stuff. It\'s just an empty cave now.'
                       )

        print_wait('You walk back out to the field.\n')
        action(enemy, weapon)

    def house(enemy, weapon):
        print_wait('You approach the door of the house.')
        print_wait('You are about to knock when the door'
                   + '  opens and out steps a ' + enemy + '.')
        print_wait('Eep! This is the ' + enemy + "'s house!")
        print_wait('The ' + enemy + ' attacks you!')
        print_wait('You feel a bit under-prepared for this,'
                   + ' what with only having a tiny dagger.'
                   )

        while True:
            choice = \
                input('Would you like to (1) fight or (2) run away?\n')

            if '1' == choice:
                fight(enemy, weapon)
                break
            elif '2' == choice:

                print_wait('You run back into the field. Luckily,'
                           + ' you don\'t seem to have been followed.\n'
                           )
                action(enemy, weapon)
                break

    field(enemy, weapon)


play_game()
