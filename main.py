# ----- Project: Quiz Game -----

# Create imports
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Write a loop to iterate over question_data
# Create a question object from each entry in question_data
# Append each question object to question_bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("👍 You have completed the quiz!")
print(f"🔢 Your final score is {quiz.quiz_score}/{quiz.question_number*10}")
