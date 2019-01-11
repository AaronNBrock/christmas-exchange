import random as random


names = [
    'Aaron',
    'Sister 1',
    'Brother 1',
    'Sister 2',
    'Mom',
    'Dad'
]

random.shuffle(names)

for idx, name in enumerate(names):
    gift_for = names[(idx + 1) % len(names)]
    partner  = names[(idx + 3) % len(names)]
    with open("{name}.txt".format(name=name), "w") as file:
        file.write("Hello, {name}!\n\nYou're buying a gift for {gift_for}.  Your shopping partner is {partner}.  Have fun!\n\n~Aaron N. Brock".format(name=name, gift_for=gift_for, partner=partner))
