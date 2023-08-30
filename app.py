from flask import Flask, render_template, request
from sqlalchemy import text
from database import engine, load_questions_from_db

app = Flask(__name__)


def load_questions_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM quiz"))
    result_all = result.all()
    questions = []
    for row in result_all:
      questions.append(row._asdict())
    return questions


@app.route("/")
def index():
  return render_template('home.html')


@app.route('/quiz')
def quiz():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM quiz"))
    questions = [row._asdict() for row in result]

  return render_template('quiz.html', questions=questions)


@app.route("/submit", methods=['POST'])
def submit():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM quiz"))
    questions = [row._asdict() for row in result]

  score = 0
  for question in questions:
    user_answer = request.form.get(question['question'])
    if user_answer == question['correct_option']:
      score += 1

  return render_template('results.html', score=score, total=len(questions))


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
