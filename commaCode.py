def comma(egg):
    message = ''
    for i in range(len(egg)):
        if i == 0:
            message = egg[0]
        elif i != len(egg) - 1:
            message = message + ', ' + egg[i]
        else:
            message = message + ', and ' + egg[i]
    return message


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))
