__author__ = 'dalton'

sentence = input("Type a sentence to be reversed: ")
translate = ''

for i in range(1, len(sentence)+1):
    translate += sentence[-i]

print(translate)