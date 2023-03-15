import pprint

message = 'Les sanglots longs des violons de l\'automne'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
