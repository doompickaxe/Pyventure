"""
text_adventure.py
Text Adventure Game
Kevin Watzal, is171322
text_adventure.py [-v]
"""
import argparse
import logging
from random import choice, randint, uniform, getrandbits

from model.farmer import Farmer
from model.rogue import Rogue
from model.sailsman import Sailsman
from model.warrior import Warrior


def preMain():
    parser = argparse.ArgumentParser(description='A text adventure game')
    parser.add_argument("-v",
                        "--verbose",
                        help="increase output verbosity",
                        action="store_true")

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)


def main():
    preMain()
    print("\nStranger: Adventurer! Nice to see you here. Please, you need to help me.")
    name = input("But first, let me know your name: ")
    player = createCharacter(name, 1)
    print(f'Stranger: Ah, yes of course! I heard of you. {player}.')
    print(f'You need to bring this letter to the king in the mountains.\n'
          f'Just follow the street and you will find it, {player.name}.\n'
          f'Now go quickly, the king needs to be informed about this.')
    beginJourney(player)


def createCharacter(name: str, level):
    clazz = choice([Farmer, Warrior, Rogue, Sailsman])
    return clazz(name, level)


def beginJourney(player):
    print('\nAs you were told, you take the letter and go ahead. After a while you come along a crossing, but '
          'you don\'t know where to go.')
    decision = validateInput("Do you take the right or left path? (type \'right\' or \'left\') ", ('right', 'left'))
    print(f'You: {player.yes}')
    if decision == 'left':
        leftPath(player)
    else:
        rightPath(player)


def fightHans(player):
    enemy = createCharacter('Hans', 1)
    winner = fight(player, enemy)
    if winner == enemy:
        print(f'You died.')
        exit(0)
    print(f'With blood on your hands, you feel more powerful now and level up.')
    player.levelUp()


def leftPath(player):
    print(f'\nYou took the left path and entered the mysterious forest.')
    print(f'As you go, somebody jumps right in front of you and wants to steal your letter.\n'
          f'There is no way around it, you have to fight him.')
    fightHans(player)
    print(f'\nYou begin to ask yourself how important that letter really is.')

    decision = validateInput("Do you want to read the letter? ", ['yes', 'no'])
    if decision == 'yes':
        readLetter(player)
    seeMountainCity(player)


def readLetter(player):
    if bool(getrandbits(1)):
        print('\tMy dear Ragnar, \n'
              '\tAs you know, your child has become crazy enough to raise an army against you.\n'
              '\tYou have to quickly make ready every man who is able to stand and prepare the city for the fight.\n'
              '\tIn love,\n\tYour sister.')
        print('As you finished reading the letter, every single word on it just vanishes.')
    else:
        print('The letter is empty.')

    decision = validateInput("Do you still want to deliver the letter? ", ['yes', 'no'])

    if decision == 'no':
        print(f'You: {player.no} this cannot be.\n'
              f'You take your sword and decide to end it right now.')
        exit(0)

    print('You hope that this is some kind of magic and continue pursuing your goal.')
    seeMountainCity(player)


def rightPath(player):
    print(f'\nYou took the right path and entered a small village.\nYou see a villager.')
    decision = validateInput("Do you want to ask him for help? (type 'yes' or 'no)", ['yes', 'no'])
    if decision == 'yes':
        print('Hey you! Where am I?')
        print('Stranger: You don\'t know that? Well ... what was the name of this place again?')
        print('Several minutes pass by as the stranger looks in the sky and thinks.')
        print('Stranger: Hello you, I didn\'t see you coming. My name is Zrek, and you are?')

        decision = validateInput("Do you want to try it again or go along? (type 'try' or 'go')", ['try', 'go'])
        if decision == 'try':
            print(f'You: Hello, I am {player.name} from {player.start}. I need to go to the mountains, to the king. '
                  f'Do you know the way?')
            print('Stranger: Ah, the king. Old and weird dude. Maybe I know the way. I need help, do you have some of your time for me?')
            decision = validateInput("Do you have time for the stranger? (type 'yes' or 'no')", ['yes', 'no'])
            if decision == 'yes':
                help(player)
            else:
                print(f'You: {player.no} I do not have time for this. I need to deliver an urgent letter.')
                print('Stranger: Then let me see what\'s inside and I can help you.')
                decision = validateInput("Do you want him to read it? ", ['yes', 'no'])
                if decision == 'yes':
                    if bool(getrandbits(1)):
                        print('Stranger: You idiot! Never should anybody read something such important! Go away!')
                        lostInTheCity(player)
                    else:
                        print('Stranger: Interesting, interesting. This is really urgent. Just follow this street, then you will see it.')
                        seeMountainCity(player)
                else:
                    if bool(getrandbits(1)):
                        print('Stranger: I understand. Just follow this path and you will see it')
                        seeMountainCity(player)
                    else:
                        print('Stranger: Okay ... then I will fight for it!')
                        fightHans(player)
                        lostInTheCity(player)
        else:
            print('You try to just go away, while you smile at him.')
            print('Stranger: Hey, I asked you something, stupid!')
            decision = validateInput("Ignore him? (type 'yes' or 'no')", ['yes', 'no'])
            if decision == 'yes':
                print('Stranger: So you want it that way!')
                print("You have to fight against him now.")
                fightHans(player)
                lostInTheCity(player)
            else:
                print(f'You: {player.yes} what\'s up? ')
                print('Stranger: Who are you and what are you doing here?')
                print(f'You: I am {player.name} from {player.start} and I am ... :{input()}')
                print('Stranger: Okay, okay, okay. Just don\'t destroy something.')
                print('He goes away.')
                lostInTheCity(player)
    else:
        lostInTheCity(player)


def help(player):
    print('Stranger: Look. It will get colder soon, but I still need to cut all this wood here. Please do it.')
    print('You do what is asked for.')
    if bool(getrandbits(1)):
        print('After hard, but honest work you level up.')
        player.levelUp()

    rand = uniform(0, 1)
    if rand < 0.33:
        print('Stranger: Thank you so much. Just follow the street and you will find it.')
        seeMountainCity(player)
    if rand < 0.66:
        print('Stranger: Hey! What are you doing here? Go away before I make you to!')
        print('You just leave, because you are so exhausted')
    else:
        print('You search for the stranger, but you cannot find him anymore.')
    lostInTheCity(player)


def lostInTheCity(player):
    print('\nYou are left in this small village and you have no idea where to go.')
    print('You try to find the way yourself.')
    if bool(getrandbits(1)):
        print('You find a street with a sign which says \'To the mountain city\'.')
        decision = validateInput('Follow this street? ', ['yes', 'no'])
        if decision == 'yes':
            seeMountainCity(player)
        else:
            print('You go a different way and meet the same stranger again. This time you don\'t speak to him. '
                  'Stranger: Sup. '
                  'You pass him.')
            differentPath(player)
    else:
        differentPath(player)



def differentPath(player):
    print('\nYou find a path and walk on it for a while. A very long while.\n'
          'You begin to start being thirsty. You see a river right next to you.')
    decision = validateInput("Drink from the water? ", ['yes', 'no'])
    if decision == 'yes':
        if bool(getrandbits(1)):
            print('You get a disease and your health halves.')
            player.health = player.health / 2
        else:
            print('You feel very refreshed now and continue walking.')
        print('You see an inn and go there. You drink beer and get to know some people.\n'
              'They know the way to the mountains and tell it to you.\n'
              'You happily follow the directions.')
        seeMountainCity(player)
    else:
        print('You begin to feel weaker, but continue walking.\n'
              'Finally you see an inn. You ran to it, try to open the door, but notice, that it is only big rock.')
        if bool(getrandbits(1)):
            print('You decide to sit down. You feel so weak, that you sleep in. But you will never wake up again.')
            exit(0)

        print('You see another Inn a bit farther away.')
        decision = validateInput("Do you run to that inn? ", ['yes', 'no'])
        if decision == 'no':
            print('You decide to sit down. You feel so weak, that you sleep in. But you will never wake up again.')
            exit(0)
        print('You run to that inn, but this time it really is one. You drink beer and get to know some people.\n'
              'They know the way to the mountains and tell it to you.\n'
              'You happily follow the directions.')
        seeMountainCity(player)


def seeMountainCity(player):
    print('\nFinally, you see the city in the mountains. But you would have to climb 1000 stairs.')
    decision = validateInput("Do you want to take the challenge and climb? ", ['yes', 'no'])
    if decision == 'yes':
        climbStairs(player)
    else:
        print("You find a magician.\n"
              "You: Hey magician! Can you teleport me to the city?\n"
              "Magician: Yes of course I can. But I am very very bored. So you have to solve a difficult, but "
              "very ancient riddle.")
        decision = validateInput("Do you want to solve the riddle? ", ['yes', 'no'])

        if decision == 'yes':
            print(f'Magician: Fantastic {player.name}!')
            guess = validateInputToInt("Which number between 1 and 3 am I thinking right now? ", 1, 3)
            if guess == randint(1, 3):
                print('Congratulations! I will see you in the city.')
                reachCity(player)
            else:
                print('Sorry. I have to fight you now.')
                fightMagician(player)
        else:
            print('Magician: Mhm. Why are people always so rude. Okay, then goodbye.')
            print('The magician disappears in a cloud.\n'
                  'You just stand here with the view of the stairs and decide to take them.')
            climbStairs(player)


def climbStairs(player):
    print('After every stair you feel more exhausted. There has to be a spell on this. You scream out of desperation.')
    print('Magician: You give up early. Normally people give up 4 stairs later under my spell.')
    decision = validateInput("Do you want to kill the magician? ", ['yes', 'no'])
    if decision == 'yes':
        fightMagician(player)
        print('You continue climbing and finally reach the city.')
        reachCity(player)
    else:
        print('Magician: I am sorry, I was being rude. Come on, you can pass now without any problems.')
        if bool(getrandbits(1)):
            print('You continue climbing, but after a few steps you see, that you are back at the beginning.')
            print('Magician: Hahahaha, you fool!')
            decision = validateInput("Do you now want to kill the magician? ", ['yes', 'no'])
            if decision == 'yes':
                fightMagician(player)
                print('You continue climbing and finally reach the city.')
                reachCity(player)
            else:
                print('Magician: Sorry, nobody has visited us for a very long time. I will now teleport us to the city.')
                reachCity(player)
        else:
            print('You continue climbing and finally reach the city.')
            reachCity(player)


def fightMagician(player):
    enemy = createCharacter('Magician', 2)
    logging.info(f'Magician has a luck of {enemy.luck}')
    winner = fight(player, enemy)
    if winner == enemy:
        print(f'You died.')
        exit(0)

    print(f'You won.\nWith blood on your hands, you feel more powerful now and level up.')
    player.levelUp()


def reachCity(player):
    print('\nYou reached the city.')
    if bool(getrandbits(1)):
        print('You reach a brothel.')
        if bool(getrandbits(1)):
            print('You go inside.')
            if bool(getrandbits(1)):
                print('You caught up a disease. Your health halves.')
                player.health = player.health / 2
        else:
            decision = validateInput("Do you want to go in? ", ['yes', 'no'])
            if decision == 'yes':
                if bool(getrandbits(1)):
                    print('You caught up a disease. Your health halves.')
                    player.health = player.health / 2
                else:
                    print('Congratulations. You level up.')
                    player.levelUp()

                if bool(getrandbits(1)):
                    print('You cannot find the letter again. You go to the boss of the brothel and demand to get it back.')
                    print('He kills you.')
                    exit(0)
        print('You leave the brothel and head to the king.')

    print('\nAs you go to the king, a soldier stops you.')
    print('Soldier: What do you want here?')
    print('You: I need to go to the king. I have an important letter for him.')
    print('Soldier: Okay. He will have time for you in two weeks.')

    decision = validateInput("Do you want to wait? ", ['yes', 'no'])
    if decision == 'yes':
        print('While you wait and visit the brothel more often, the city gets attacked and everybody gets killed.')
        exit(0)

    print('You: You need to understand ...')
    print('Soldier: You need to wait.')

    rand = uniform(0, 1)

    if rand < 0.25:
        print('All of a sudden the soldier has a heart attack and you run to the king.')
        king(player)
    if rand < 0.5:
        print('The king passes by and sees your letter.')
        print('King: Hey! Where did you get the letter from? I don\'t have time for this. Just follow me. Let\'s go.')
        king(player)
    if rand < 0.75:
        print('You beg him on your knees. You make yourself to a fool. You do whatever he asks for. He lets you pass.')
        king(player)

    print('You need to fight against him.')
    soldier = createCharacter('Soldier', 3)
    winner = fight(player, soldier)
    if winner == soldier:
        print('You die.')
        exit(0)

    print('You win.')
    player.levelUp()
    king(player)


def king(player):
    print('You finally reached the king.')
    print('You: King I have a very urgent letter for you, given to me by a stranger.')
    print('King: Well, then let\'s see.')

    if bool(getrandbits(1)):
        print('King: What is this? This letter is empty! Soldiers, kill this man.')
        exit(0)

    print('King: Thank you very much adventurer. This will save us and the whole city.')
    print('You are allowed to live and continue your travels.')
    print(player)
    print(f'Your luck was: {player.luck}')
    exit(0)


def fight(char1, char2):
    damage = validateInputToInt("You can choose, how hard your hits will be. Say a number between 10 and 50: ", 10, 50)
    while char1.health > 1 and char2.health > 1:
        makeHit(char1, char2, damage)
        if char2.health < 1:
            break
        makeHit(char2, char1, damage)
    return returnWinner(char1, char2)


def validateInput(text, possibleSolutions):
    while True:
        user_input = input(text)
        if user_input in possibleSolutions:
            return user_input


def validateInputToInt(text, min, max):
    while True:
        try:
            user_input = int(input(text))
            if min <= user_input <= max:
                return user_input
            else:
                print('Please stay within the boundaries.')
        except:
            print('Please enter a number.')


def makeHit(attacker, defender, damage):
    if uniform(0, 1) < attacker.luck:
        hit1 = damage + (randint(0, 10) - 5)
        logging.info(f'{attacker.name} hit with {hit1}')
        defender.health -= damage
    else:
        logging.info(f'{attacker.name} missed')


def returnWinner(char1, char2):
    if char1.health > char2.health:
        return char1
    else:
        return char2


if __name__ == '__main__':
    main()
