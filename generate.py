import random

coin = random.choice(["heads", "tails"])

number = random.randint(0, 10)

cards = ["jack", "king", "queen"]

random.shuffle(cards);

print(coin)

print(number)

for card in cards:
  print(card)