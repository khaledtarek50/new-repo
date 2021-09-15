import random

questions = [
    ['What\'s your name', 'Ahmed'],
    ['How old are you', '22'],
    ['Where are you from', 'ABCD'],
]

random.shuffle(questions)
num_tries = 0
max_tries = 3
current_idx = 0
change = 10

def ask(question):
    return input("{}: ".format(question))


while True:
    if not num_tries < max_tries:
        print('You\'ve failed 3 times in a row. ')
        break

    if current_idx > len(questions) - 1:
        print('Done.')
        break

    question, correct_answer = questions[current_idx]
    print(correct_answer)
    user_answer = ask(question)

    if user_answer.lower() != correct_answer.lower():
        num_tries += 1
    else:
        print('Correct!')
        current_idx += 1
