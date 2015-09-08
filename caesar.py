__author__ = 'dalton'

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(message, key):
    result = ''
    for i in message:
        if i in letters:
            num = letters.find(i)
        if i == ' ':
            result += ' '
        elif (num + key) < len(letters):
            result += letters[num+key]
        else:
            result += letters[(num+key) - len(letters)]
    return result

def decrypt(message, key):
    result = ''
    for i in message:
        if i in letters:
            num = letters.find(i)
        if i == ' ':
            result += ' '
        else:
            result += letters[num-key]
    return result



if __name__ == '__main__':
    message = input('Enter message: ').upper()
    enc_or_dec = input('(E)ncrypt or (d)ecrypt? ').lower()
    key = int(input('Enter key: '))

    if enc_or_dec in ('encrypt', 'e'):
        print(encrypt(message, key))
    elif enc_or_dec in ('decrypt', 'd'):
        print(decrypt(message, key))