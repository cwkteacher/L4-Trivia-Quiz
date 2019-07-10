import random as rdm

questions = [["What does CPU stand for",'Central Processing Unit'],["How do you write 9 in binary",'1001'],["What does RAM stand for",'Random Access Memory']]

def main():
    print('Welcome to CS Trivia:\n')
    correct = 0
    incorrect = 0
    while len(questions) > 0:
        question = rdm.choice(questions)
        answer = input('Q: {}?\n'.format(question[0]))
        if answer.lower() == question[1].lower():
            print('Correct!')
            correct += 1
        else:
            print('I\'m sorry that is incorrect! The correct answer was {}.'.format(question[1]))
            incorrect += 1
        questions.remove(question)
    print('\nYou got {}% of the questions correct.'.format(int((correct/(correct+incorrect))*100)))

if __name__ == '__main__':
    main()