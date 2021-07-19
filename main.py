# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 2019-09-03
from classes.Questions import Questions


if __name__ == "__main__":
    questions = Questions()
    print("You have been assigned to the category  :",questions.record_answers(questions.run_questions()))
