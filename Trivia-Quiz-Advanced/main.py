import random as rdm

questions = {"What does CPU stand for":['A: Computer Program Unit','B: Central Processing Unit','C: Central Program Unit','D: Computer Processing Unit','B'],
            "How do you write 9 in binary":['A: 1001','B: 1100','C: 1011','D: 1111','A'],
            "What does RAM stand for":['A: Random Access Memory','B: Random Array Memory','C: Random Access Microchip','D: Really Awesome Mouse','A']}

def main():
    print('Welcome to CS Trivia:\n')
    correct = 0
    incorrect = 0
    while len(questions) > 0:
        question = rdm.choice(list(questions.keys()))
        answer = input('Q: {}?\n\n'.format(question)+'\n'.join(questions[question][a] for a in range(4)))
        if answer.lower() == questions[question][4].lower():
            print('Correct!\n')
            correct += 1
        else:
            print('I\'m sorry that is incorrect! The correct answer was {}.\n'.format(questions[question][4]))
            incorrect += 1
        del questions[question]
    print('You got {}% of the questions correct.'.format(int((correct/(correct+incorrect))*100)))

if __name__ == '__main__':
    main()
