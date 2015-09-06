__author__ = 'dalton'

def main():
    message = input("Enter your text: ")
    key = int(input("Enter your key: "))

    translate(message, key)

def translate(message, key):
    counter = len(message)
    answer = ''
    for i in range(key):
        jump = i
        while jump < counter:
            answer += message[jump]
            jump += key

    print(answer + '|')

if __name__ == '__main__':
    main()

