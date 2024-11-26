print('Emoji Converter lol')

message = input("type> ")

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

print('Result: ' + output)