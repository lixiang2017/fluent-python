import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(FrenchDeck().ranks)
print(FrenchDeck().suits)

# __getitem__
print(deck[0])
print(deck[1])
print(deck[3])
print(deck[-1])
#print(deck[:])

# random choice
from random import choice
print("random choice:")
print(choice(deck))
print(choice(deck))
print(choice(deck))

# top 3
print("Top 3 :",deck[:3])

# only 'A'
print("Only Ace :", deck[12::13])

# iterable
for card in deck:
    print(card)

# reversed iterable
for card in reversed(deck):
    print(card)

# in
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)



