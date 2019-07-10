import random as rdm

questions = ["What does CPU stand for","How do you write 9 in binary","What does RAM stand for"]
answers = ['Central Processing Unit','1001','Random Access Memory']

def main():
    print('Welcome to CS Trivia:\n')
    correct = 0
    incorrect = 0
    while len(questions) > 0:
        idx = rdm.randint(0, len(questions)-1)
        print('Q: {}?'.format(questions[idx]))
        answer = input()
        if answer.lower() == answers[idx].lower():
            print('Correct!')
            correct += 1
        else:
            print('I\'m sorry that is incorrect! The correct answer was {}.'.format(answers[idx]))
            incorrect += 1
        del questions[idx]
        del answers[idx]
    print('\nYou got {}% of the questions correct.'.format(int((correct/(correct+incorrect))*100)))

if __name__ == '__main__':
    main()
