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


# 香港称"啤酒牌"
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

# sort 2最小、A最大 黑桃最大、红桃次之、方块再次、梅花最小
# 点数优先：先比较点数，再比较花色
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
# print(suit_values)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key = spades_high):
    print(card)

# 洗牌 __setitem__
