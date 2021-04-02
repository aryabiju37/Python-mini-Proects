class Card:
    original_suit=["Hearts","Diamonds","Clubs","Spades"]
    original_value=["A","J","Q","K","10","9","8","7","6","5","4","3","2"]
    def __init__(self,value,suit):
        if suit not in Card.original_suit and value not in Card.original_value:
            raise ValueError("Unacceptable Suit and Value Type")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value,self.suit)

    def create_decks(self,original_suit,original_value):
        deck=[]
        deck= [Card(value,suit) for suit in original_suit for value in original_value]
        # for suit in original_suit:
        #     for value in original_value:
        #         Card(value,suit)

        return deck


C = Card("A","Clubs")
print(C.create_decks(C.original_suit,C.original_value))

 
# class Deck(Card):
#     drawn_cards = 0
#     deck = Card.create_decks(Card,Card.original_suit,Card.original_value)


#     def __init__(self,Card):
#         self.Card = Card
        

#     def __rep__(self):
        
#         return "Deck of {} cards".format(len(Deck.deck))

#     def _deal(self,rm_cards):
#         dealt_cards=[]
#         if rm_cards <= len(Deck.deck):
#             for i in range(rm_cards):
#                 dealt_cards.append(Deck.deck.pop(i))
#         elif rm_cards>len(Deck.deck):
#             Deck.deck.clear()
#         else:
#             raise ValueError("All cards have been dealt")
#         Deck.drawn_cards = len(Deck.deck)
#         return dealt_cards

#     def deal_card(self,num_card=1):
#         dealt_card=0
#         if num_card>1:
#             raise ValueError("Deals only one card")
#         dealt_card = self._deal(num_card)
#         return dealt_card
    
#     def deal_hand(self,number):
#         return self._deal(number)
    


#     def shuffle(self):
#         if len(Deck.deck)<52:
#             raise ValueError("Only full decks can be shuffled")
#         return Deck.deck.sort()            



#     def count(self):
#         return Deck.drawn_cards

# C = Card("Clubs","A")
# # print(C.create_decks(C.original_suit,C.original_value))
# d = Deck(C)
# print(d._deal(10))


