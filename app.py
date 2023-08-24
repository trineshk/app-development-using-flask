from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
  {
    "question": "What is the capital of India?",
    "options": ['Delhi', 'Punjab', 'Mumbai', 'Kashmir'],
    "correct_answer": 'Delhi'
  },
  {
    "question": "What is the national animal of India?",
    "options": ['Lion', 'Cheetah', 'Tiger', 'Elephant'],
    "correct_answer": 'Tiger'
  },
  {
    "question": "2 + 5?",
    "options": [6, 7, 0, 4],
    "correct_answer": '7'
  },
]


@app.route("/")
def index():
  return render_template('home.html', questions=questions)


@app.route("/quiz")
def quiz():
  return render_template('quiz.html', questions=questions)


@app.route("/submit", methods=['POST'])
def submit():
  score = 0
  for question in questions:
    user_answer = request.form.get(question['question'])
    if user_answer == question['correct_answer']:
      score += 1
    print(score)

  return render_template('results.html', score=score, total=len(questions))


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
