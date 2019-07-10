class Quiz_Question:
    def __init__(self, question = "", answers = [""], correct = 0):
        self.question = question
        self.answers = answers
        self.correct = correct
    
    def print_question(self):
        print("Question:  {}".format(self.question))
    
    def print_answers(self):
        for i in range(len(self.answers)):
            print("{}:  {}".format(i + 1, self.answers[i]))
    
    def ask_question(self):
        self.print_question()
        self.print_answers()
        choice = int(input("Enter a number to make a choice.  "))
        if choice == self.correct:
            return True
        else:
            return False
    
def make_quiz():
    questions = []
    
    # Question 1
    question = "Link is a character from which game series?"
    answers = ["Tomb Raider", "Legend of Zelda", "Super Mario Bros", "Pokemon"]
    questions.append(Quiz_Question(question, answers, 2))
    
    # Question 2
    question = "Who was the first computer programmer?"
    answers = ["Ada Lovelace", "Charles Babbage", "Grace Hopper", "Alan Turing"]
    questions.append(Quiz_Question(question, answers, 1))
    
    # Question 3
    question = "What is 'pixel' short for?"
    answers = ["pixel - it's not short for anything", "Edward Pixelli", "pixelized point", "picture element"]
    questions.append(Quiz_Question(question, answers, 4))
    
    return questions

def play_game(questions):
    correct = 0
    
    for question in questions:
        if question.ask_question():
            print("Correct!")
            correct += 1
        else:
            print("Wrong")
    
    print("You got {}/{} correct!".format(correct, len(questions)))

if __name__ == "__main__":
    questions = make_quiz()
    play_game(questions)
