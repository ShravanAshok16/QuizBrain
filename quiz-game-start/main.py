from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = Quizbrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
if quiz_brain.score < 5:
    print("You could do better next time")
    print(f"Your Final Score is : ", {quiz_brain.score}, "/", {quiz_brain.question_number})
elif quiz_brain.score >= 5:
    print("You did great!")
    print(f"Your Final Score is : ", {quiz_brain.score}, "/", {quiz_brain.question_number})



