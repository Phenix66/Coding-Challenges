#!/usr/bin/python
import sys
import random

class Orc:
    def __init__(self, name, health, atk_dmg, atk_speed):
        self.name = name
        self.health = health
        self.atk_dmg = atk_dmg
        self.atk_speed = atk_speed

    def attack(self, attacker, target):
        # Damage calculation is made by taking a random roll and multiplying it by attack damage.
        # Higher attack speeds allow for more hits
        dmg = (random.randint(1, 5) * self.atk_dmg) * self.atk_speed
        target.take_dmg(dmg)
        if attacker == target:
            print "\n%s attacked himself for %d!" % (attacker.name, dmg)
            if target.health > 0:
                print "%s has %d health left." % (target.name, target.health)
        else:
            print "\n%s attacked %s for %d" % (attacker.name, target.name, dmg)
            if target.health > 0:
                print "%s has %d health left." % (target.name, target.health)

    def take_dmg(self, dmg):
        self.health -= dmg

    def dead_yet(self):
        if self.health <= 0:
            print "%s has fallen on the battlefield!" % (self.name)
            return True
        else:
            return False

class LargeOrc(Orc):
    def __init__(self, name):
        Orc.__init__(self, name, 100, 5, 1)

class SmallOrc(Orc):
    def __init__(self, name):
        Orc.__init__(self, name, 75, 2, 3)

def choose_tgt(players, attacker):
    proceed = False
    while proceed == False:
        counter = 1
        print "\n"
        for x in players:
            if x != players[attacker]:
                print " Player %s) %s  HP:%3s" % (counter, x.name, x.health)
            counter += 1
        try:
            target = int(raw_input("\n%s please choose a target (1-%s): " \
                                % (players[attacker].name, len(players))))-1
            if target == attacker:
                confirm = raw_input("Are you sure you want to attack yourself stupid? ")
                if confirm.lower() == "y" or confirm.lower() == "yes":
                    proceed = True
            else:
                proceed = True
        except ValueError:
            print "Use the corresponding numbers only"
        except KeyboardInterrupt:
            print "\nSurrender detected! Shame!"
            sys.exit(0)
    return target

if __name__ == "__main__":
    players = []
    counter = 1
    while True:
        try:
            inputName = raw_input("Enter Player %s's orc name: " % (counter))
            inputClass = raw_input("Small Orc or Large Orc? ")
            if inputClass.lower() == "small":
                players.append(SmallOrc(inputName))
            elif inputClass.lower() == "large":
                players.append(LargeOrc(inputName))
            else:
                print "Invalid class selection"
            counter += 1
            if len(players) > 1:
                more = raw_input("Add another player? (y/N) ")
                if more.lower() == "y" or more.lower() == "yes":
                    pass
                else:
                    break
        except KeyboardInterrupt:
            print "\nWe decided against war. Pacifists are boring."
            sys.exit(0)

    while True:
        if len(players) == 1:
           break
        attacker = random.randint(0, len(players)-1)
        target = choose_tgt(players, attacker)

        players[attacker].attack(players[attacker], players[target])
        if players[target].dead_yet():
            players.pop(target)

    print "\nThe Great War is over!"
    print "%s receives all the glory!" % (players[0].name)
