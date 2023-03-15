catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop).')
    name = input()
    if name == '':  # check stop
        break
    if name in catNames:  # check duplicates
        print('You already entered a cat named'+str(name))
        continue
    else:
        catNames += [name]  # List concatenation
print('The cat names are:')
for spam in catNames:
    print('   ' + spam)
