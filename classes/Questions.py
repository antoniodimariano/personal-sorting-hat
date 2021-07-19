# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 2019-09-03
import random


class Questions:

    def __init__(self):

        self.questions_and_answers = {
            0: {
                "question": "Four boxes are placed before you. Which would you try and open?\n"
                            "(a) The small tortoiseshell box, embellished with gold, inside which some small creature seems to be squeaking.\n"
                            "(b) The gleaming jet black box with a silver lock and key, marked with a mysterious rune that you know to be the mark of Merlin.\n"
                            "(c) The ornate golden casket, standing on clawed feet, whose inscription warns that both secret knowledge and unbearable temptation lie within.\n"
                            "(d) The small pewter box, unassuming and plain, with a scratched message upon it that reads ‘I open only for the worthy.’\n\n"
            },
            1: {
                "question": "You and two friends need to cross a bridge guarded by a river troll who insists on fighting one of you before he will let all of you pass. Do you\n"
                            "(a) Attempt to confuse the troll into letting all three of you pass without fighting?\n"
                            "(b) Suggest drawing lots to decide which of you will fight?\n"
                            "(c) Suggest that all three of you should fight (without telling the troll)?\n"
                            "(d) Volunteer to fight?\n\n"
            },
            2: {
                "question": "Once every century, the Flutterby bush produces flowers that adapt their scent to attract the unwary. If it lured you, it would smell of\n"
                            "(a) A crackling log fire\n"
                            "(b) The sea\n"
                            "(c) Fresh parchment\n"
                            "(d) Home\n\n"
            },
            3: {
                "question": "Which of the following do you find most difficult to deal with?\n"
                            "(a) Hunger\n"
                            "(b) Cold\n"
                            "(c) Loneliness\n"
                            "(d) Boredom\n\n"
            },
            4: {
                "question": "Four goblets are placed before you. Which would you choose to drink?\n"
                            "(a) The foaming, frothing, silvery liquid that sparkles as though containing ground diamonds.\n"
                            "(b) The smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums.\n"
                            "(c) The golden liquid so bright that it hurts the eye, and which makes sunspots dance all around the room.\n"
                            "(d) The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions.\n\n"
            }

        }
        self.user_answers = {}
        self.categories = {"a": "Ravenclaw", "b": "Slytherin", "c": "Hufflepuff", "d": "Gryffindor"}
        self.results = {"a": 0, "b": 0, "c": 0, "d": 0}

    def run_questions(self) -> dict:
        """
        This functions generates a list of random and unique numbers in the range of 0-4.
        Then each item in the list is used to select the question to ask
        At the end, the results dictionary is returned
        :return: results dictionary
        """
        questions_sequence = random.sample(range(0, 5), 5)
        for i in questions_sequence:
            self.ask_question(question_id=i)
        return self.user_answers

    def ask_question(self, question_id):
        """
        This functions asks the question selected by the given question_id
        If the answer is not valid, the same question will be asked again until a valid answer will be provvided.

        :param question_id:
        :return:
        """
        allowed_answers = ['a', 'b', 'c', 'd']
        answer = input(self.questions_and_answers[question_id].get('question'))
        if answer in allowed_answers:
            print("Your answer:", answer)
            self.user_answers[question_id] = answer
        else:
            print("Please type a,b,c or d\n")
            self.ask_question(question_id=question_id)

    def record_answers(self, answers):
        """
        This functions counts and stores the answers in the right category
        At the end, it returns the category key with has the maximum value
        :param answers:
        :return:
        """
        try:
            for answer in answers.values():
                if answer in self.categories.keys():
                    self.results[answer] += 1
                else:
                    print("No matching between answer and category")
                    exit(-1)

            return self.categories[max(self.results, key=self.results.get)]
        except Exception as error:
            print("Exception recording answers:", error)
            exit(-1)
