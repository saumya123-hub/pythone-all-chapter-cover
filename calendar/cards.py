import itertools, random
# form deck of cards
deck = list(itertools.product(range(1,4),["spade","heart","diamond","club"]))
# shuffle the cards
random.shuffle(deck)
# draw five cards
print("your combination of cards is: ")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])