#!/usr/bin/env python3
letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}


def score(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def replacement(hand):
    if hand == "":
        return [""]
    return [x+y for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
            for y in replacement(hand[1:])]

print(replacement("TJKQ2"))

def classify(hand):
    return max(map(score, replacement(hand)))

def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])

print(strength("TTJJX"))


plays = []
for line in open(0):
    hand, bid = line.split()
    plays.append((hand, int(bid)))

print(plays)

plays.sort(key=lambda play: strength(play[0]))
print(plays)

total = 0
for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid
print(total)
