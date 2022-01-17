class QuizBrain:
    def __init__(self, question_obj_list):
        self.quesiton_number = 0
        self.score = 0
        self.quesiton_list = question_obj_list

    def is_questions_left(self):
        return self.quesiton_number < len(self.quesiton_list)

    def next_question(self):
        question_obj = self.quesiton_list[self.quesiton_number]
        self.quesiton_number += 1
        question = f"Q.{self.quesiton_number}. {question_obj.question} (True/False): "
        user_input = input(question)
        self.check_answer(user_input, question_obj.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.quesiton_number}")
        print("\n")

    