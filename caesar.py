__author__ = 'dalton'

message = input('Enter message: ').upper()
enc_or_dec = input('(E)ncrypt or (d)ecrypt? ').lower()
key = int(input('Enter key: '))
result = ''

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if enc_or_dec in ('encrypt', 'e'):
    for i in message:
        if i in letters:
            num = letters.find(i)
        if i == ' ':
            result += ' '
        elif (num + key) < len(letters):
            result += letters[num+key]
        else:
            result += letters[(num+key) - len(letters)]
elif enc_or_dec in ('decrypt', 'd'):
    for i in message:
        if i in letters:
            num = letters.find(i)
        if i == ' ':
            result += ' '
        else:
            result += letters[num-key]


print(result)