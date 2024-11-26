# Turning my emoji converter program to be re-usable
# inputs and outputs should not be re-usable in functions

def emojify(string):
    words = message.split() # spilts the message in multiple sections and makes a list
    emoji_dict = {
    ':)': '😊',
    ':D': '😃',
    ';)': '😉',
    ':(': '😞',
    ':/': '😕',
    ':P': '😛',
    ':o': '😲',
    'B)': '😎',
    ':|': '😐',
    'XD': '😆',
    ':*': '😘',
    '<3': '❤️',
    ':@': '😡',
    ':S': '😖',
    'O:)': '😇',
    '>:(': '😠',
    ':\'(': '😢',
    'O.o': '😳',
    ':$': '😳',
    ':3': '😊',
    ':^)': '😊',
    '8)': '😎',
    '8D': '😁',
    '=)': '😊',
    '=D': '😃',
    '=3': '😊',
    ':-)': '😊',
    ':-(': '😞',
    ':-D': '😃',
    ':-P': '😛',
    ':-o': '😲',
    ':-|': '😐',
    ':-/': '😕',
    ':-*': '😘',
    ':-@': '😡',
    ':-S': '😖',
    '>.<': '😣'}

    output = ''
    for word in words:
        output += emoji_dict.get(word, word) + ' '
    return output


print('Emoji Converter lol')
message = input("type> ")
print(emojify(message))


# now this is a re-usable program in any application