# Blackjack card game

import deck_of_cards
import random

class Player(object):
    def __init__(self,name):
        self.bankroll=1000
        self.name=name
        self.cards=[]
    def reset_cards(self):
        self.cards=[]
    def addChips(self,chips):
        self.bankroll+=chips
    def removeChips(self,chips):
        self.bankroll-=chips
    def recieves_card(self,card):
        self.cards.append(card)
    def show_cards(self):
        print "%s's card(s): " %self.name
        print self.cards
    def cards_sum(self):
        cards_sum=0
        for i in range(len(self.cards)):
            card=self.cards[i][0].upper()
            if card=='JACK' or card=='QUEEN' or card=='KING':
                cards_sum+=10
            elif card=='ACE':
                if cards_sum+11>21:
                    cards_sum+=1
                else:
                    cards_sum+=11
            else:
                cards_sum+=int(card)
        return cards_sum
    def BJ_check(self):
        has_ACE=False
        has_TEN_card=False
        for i in range(len(self.cards)):
            card=self.cards[i][0].upper()
            if card=='ACE':
                has_ACE=True
            elif card=='10' or card=='JACK' or card=='QUEEN' or card=='KING':
                has_TEN_card=True
        return has_ACE and has_TEN_card
    def Bust_check(self):
        if self.cards_sum() > 21 :
            return True
        else:
            return False

def first_hand_BJ_check(dealer,player):
    if dealer.BJ_check() and p.BJ_check():
        print "It's a PUSH"
        dealer.show_cards()
        p.show_cards()
        return True
    if dealer.BJ_check():
        print "Dealer got BlackJack!"
        dealer.show_cards()
        player.removeChips(bet)
        return True
    if player.BJ_check():
        print "You got BlackJack!"
        player.addChips(bet)
        return True
    return False

# MAIN part

print "Welcome to Blackjack card game by Marko Stanojlovic! Good luck! \n\n"
player_name=raw_input('Please enter player name: ')
print "\nHello %s! You recieved 1000 chips." %player_name
p=Player(player_name)
dealer=Player('Dealer')

# one deck of cards for dealing
d=deck_of_cards.Deck_of_cards()

while True:
    # choosing new hand or to quit game #
    continue_game=raw_input("New hand? [y/n]: ")
    if continue_game=='n':
        print "\nBye.\n"
        break
    # reset cards
    dealer.reset_cards()
    p.reset_cards()
    # check if there are at least 10 more cards left in the deck
    if len(d.deck)<10:
        print "No more cards in the deck. Game over."
        break
    # notifying player about new bankroll state #
    # check if bankroll not empty and if possible to place that bet #
    if p.bankroll>0:
        print "Bankroll: %s \n" %p.bankroll
        while True:
            try:
                bet=int(raw_input('Place a bet:'))
            except:
                print "You didn't enter a number! Whole bankroll is you bet in that case."
                bet=p.bankroll
            if bet<=p.bankroll:
                break
            print "Not enough chips in the bankroll. Please choose another bet."
    else:
        print "Empty bankroll. Game over."
        break
    # deal part
    dealer.recieves_card(d.choose_random_card())
    dealer.show_cards()
    p.recieves_card(d.choose_random_card())
    p.recieves_card(d.choose_random_card())
    p.show_cards()
    dealer.recieves_card(d.choose_random_card())
    if first_hand_BJ_check(dealer,p):     # check if Dealer or player got the BJ in first hand
        continue
    # Player action
    # Hit loop
    while True:
        action=raw_input("Hit or Stand?:")
        player_bust=False
        if action[0].upper()=='H':
            p.recieves_card(d.choose_random_card())
            p.show_cards()
            if p.Bust_check():
                player_bust=True
                print "\n*** Bust! *** Cards sum: %s \n" %p.cards_sum()
                dealer.show_cards()
                p.show_cards()
                p.removeChips(bet)
                break
        else:
            break
    if player_bust:
        continue
    # Stand loop
    while True:
        state=''
        dealer.recieves_card(d.choose_random_card())
        dealer.show_cards()
        # check if sum >16, win, loose, push event occured
        if dealer.Bust_check():
            state='WIN'
        elif dealer.cards_sum()>=16:
            if dealer.cards_sum()>p.cards_sum():
                state='LOOSE'
            elif dealer.cards_sum()==p.cards_sum():
                state='PUSH'
            else:
                state='WIN'
        if state=='WIN':
            print "You win!"
            p.addChips(bet)
            break
        elif state=='LOOSE':
            print "You loose!"
            p.removeChips(bet)
            break
        elif state=='PUSH':
            print "It's a push!"
            break
