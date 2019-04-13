# card game

from random import shuffle

#two useful variables for creating cards.
SUITE="H D S C".split()
RANKS="2 3 4 5 6 7 8 9 10 J Q K A".split()

# mycards=[(s,r) for s SUITE for r in RANKS] same as below
#
# mycards=[]
# for r in RANKS:
#     for s in SUITE:
#         mycards.append((s,r))
class Deck:
    """
    This is a deck class. This object will create a deck of cards to initaite
    play. You can then use this Deck list of cards to split in half and give
    to the players. It will use SUITE and RANKS to create the deck. It should
    also have a method for splitting/cutting the deck in half and shuffling
    the deck.
    """
    def __init__(self):
        print("creating new order deck!")
        self.allcards=[(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("shuffling deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return(self.allcards[:26],self.allcards[26:])


class Hand(object):
    """
    This is hand class. Each player has a hand andd can add or remove
    cards from that hand. There should be an add and remove card method here.
    """
    def __init__(self,cards):
        self.cards=cards
    def __str__(self):
        return "contains {} cards".format(len(self.cards))
    def add(self):
        self.cards.extend(added_cards)
    def remove_cards(self):
        return self.cards.pop()


class Player:
    """
    This is player class, which takes in a name and an instance of a hand
    class object.The player can then play cards and check if they still hace cards.
    """
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    def play_card(self):
        drawn_card=self.hand.remove_cards()
        print("{} has placed: ".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    def remove_war_card(self):
        war_cards=[]
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Return true if player still has cards left
        """
        return len(self.hand.cards)!=0

##########################################################
print("Welcome to war, lets begin...")
#create new deck and split it in half:
d=Deck()
d.shuffle()
half1,half2=d.split_in_half()

#create both players!
comp=Player("computer",Hand(half1))

name=input("what is your name?")
user=Player(name,Hand(half2))

total_rounds=0
war_count=0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("time for new round!")
    print("here are he current standings")
    print(user.name+"has the count: "+str(len(user.hand.cards)))
    print(comp.name+"has the count: "+str(len(comp.hand.cards)))
    print("play a card!")
    print("\n")

    table_cards=[]

    c_card=comp.play_card()
    p_card=user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1]==p_card[1]:
        war_count +=1

        print("war!")

        table_cards.extend(user.remove_war_card())
        table_cards.extend(comp.remove_war_card())

        if RANKS.index(c_card[1])<RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1])<RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("game over, number of rounds:"+str(total_rounds))
print("a war happened"+str(war_count)+"times")
print("Does the computer still has cards? ")
print(str(comp.still_has_cards()))
print("Does the human still has cards? ")
print(str(user.still_has_cards()))
