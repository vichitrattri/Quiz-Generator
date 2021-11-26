# ----- Project: Quiz Game -----

# Create a QuizBrain class with __init__ method having two attributes: question_number and question_list
class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.quiz_score = 0

    # Return True: if question_list still has questions.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True/False: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.quiz_score += 10
            print("✅ You got it right!")
        else:
            print("❌ Your answer is wrong.")

        print(f"➡ The right answer is {correct_answer}")
        print(f"❔ Your score is: {self.quiz_score}/{self.question_number*10}\n")
