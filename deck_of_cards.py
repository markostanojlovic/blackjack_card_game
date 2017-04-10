# Deck of cards class in Python
import random
class Deck_of_cards(object):

    def __init__(self):
        self.deck=[]
        for sign in ['hrt','dmd','clb','pik']:
            for i in range(1,14):
                if i==1:
                    self.deck.append(('ace',sign))
                elif i==11:
                    self.deck.append(('jack',sign))
                elif i==12:
                    self.deck.append(('queen',sign))
                elif i==13:
                    self.deck.append(('king',sign))
                else:
                    self.deck.append((str(i),sign))

    def choose_random_card(self):
        # randomly pop one of the cards left in the deck
        # if deck is empty return False
        if len(self.deck)==0:
            return False
        random_index=random.randint(0,len(self.deck)-1)
        card=self.deck.pop(random_index)
        return card

    def show_card(self):
        card=self.choose_random_card()
        if card==False:
            print "No more cards in the deck. Empty deck."
            return 1
        show=card[0].upper()
        if card[1]=='hrt':
            show=show+' - HEARTS'
        elif card[1]=='dmd':
            show=show+' - DIAMONDS'
        elif card[1]=='clb':
            show=show+' - CLUBS'
        elif card[1]=='pik':
            show=show+' - PIKES'
        print show
# testing
# d1=Deck_of_cards()
# for i in range (1,55):
#     d1.show_card()
